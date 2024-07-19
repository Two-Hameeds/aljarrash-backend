from django.forms.models import model_to_dict
from django.contrib.auth import login
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import Group

from .models import (
    Employee,
    Client,
    Project,
    Attachment,
    Comment,
    TableView,
    UseTypes,
    BaladyProject,
    LandSurveyProject,
    SortingDeedsProject,
    GlobalID,
)
from .serializers import (
    EmployeeSerializer,
    RegisterSerializer,
    RemoveTokensSerializer,
    ClientSerializer,
    ProjectSerializer,
    AttachmentSerializer,
    CommentSerializer,
    TableViewSerializer,
    BaladyProjectSerializer,
    LandSurveyProjectSerializer,
    SortingDeedsProjectSerializer,
    GlobalIDSerializer
)
from .permissions import HasGroupPermission

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from django_filters.rest_framework import DjangoFilterBackend

from openpyxl import Workbook


class EmployeesViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["username", "email"]

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        if data.get("password") == None:
            data["password"] = instance.password

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.save()

        return Response(serializer.data)
    
class EngineersView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        response = { }
        for group in groups:
            Employee.objects.filter(groups=group)
            serializer = Employee.objects.filter(groups=group).values('id', 'username')
            response[group.name] = serializer
            
        return Response(response)


class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        request.data["username"] = request.data["username"].lower().strip()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.save()

        return Response(
            {
                "employee": EmployeeSerializer(
                    employee, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(employee)[1],
            }
        )


class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        request.data["username"] = request.data["username"].lower().strip()
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.validated_data["user"]
        login(request, employee)
        response = super(LoginAPI, self).post(request, format=None)
        if response.status_code == 200:
            response.data["is_superuser"] = employee.is_superuser
            response.data["is_staff"] = employee.is_staff
        return response


class RemoveTokensAPI(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = RemoveTokensSerializer

    def post(self, request, format=None):
        if not request.user.is_staff:
            return Response(
                {"message": "You are not authorized to perform this action"}, status=403
            )
        user = Employee.objects.get(username=request.data["username"])
        AuthToken.objects.filter(user=user).delete()
        return Response({"message": "Tokens removed successfully"})


class ClientsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by("moved_at")
        return queryset

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        current_stage = instance.current_stage
        new_stage = data.get("current_stage")

        if data.get("current_stage") == None:
            data["current_stage"] = instance.current_stage
        if data.get("project_name") == None:
            data["project_name"] = instance.project_name
        if data.get("project_type") == None:
            data["project_type"] = instance.project_type
        if data.get("use_type") == None:
            data["use_type"] = instance.use_type

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        if current_stage != data.get("current_stage"):
            instance.moved_at = timezone.now()
            if instance.history == None:
                instance.history = []
            instance.history.append(
                {"moved_by": str(self.request.user), "moved_at": str(timezone.now()), "from": current_stage, "to": new_stage}
            )
        instance.save()
        return Response(serializer.data)

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["current_stage"]


class CopyProjectsView(APIView):
    def post(self, request):
        ids = request.data.get("ids")
        stage = request.data.get("stage")

        if not ids or not stage:
            return Response({"message": "ids and stage are required"}, status=400)

        try:
            projects = Project.objects.filter(id__in=ids)
            new_projects = []
            for project in projects:
                project.id = None
                project.current_stage = stage
                project.created_at = timezone.now()
                project.moved_at = timezone.now()
                project.save()
                new_projects.append(project)

            serializer = ProjectSerializer(new_projects, many=True)

            return Response(serializer.data, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=400)


class CopyBaladyProjectsView(APIView):
    def post(self, request):
        ids = request.data.get("ids")
        path = request.data.get("path")

        if not ids or not path:
            return Response({"message": "ids and path are required"}, status=400)

        try:
            projects = BaladyProject.objects.filter(id__in=ids)
            new_projects = []
            for project in projects:
                project.id = None
                project.path = path
                project.created_at = timezone.now()
                project.moved_at = timezone.now()
                project.save()
                new_projects.append(project)

            serializer = BaladyProjectSerializer(new_projects, many=True)

            return Response(serializer.data, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=400)


class ExportProjectsView(APIView):
    def get(self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        if not start_date or not end_date:
            return Response(
                {"message": "start_date and end_date are required"}, status=400
            )

        try:
            start_date = timezone.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = timezone.datetime.strptime(end_date, "%Y-%m-%d").date()
        except:
            return Response({"message": "Invalid date format"}, status=400)

        projects = Project.objects.filter(created_at__range=(start_date, end_date))
        serializer = ProjectSerializer(projects, many=True)

        wb = Workbook()
        ws = wb.active
        ws.title = "Projects"

        headers = ["id", "project_name", "project_type", "use_type", "current_stage"]
        ws.append(headers)

        for project in projects:
            ws.append(
                [
                    project.id,
                    project.project_name,
                    project.project_type,
                    project.use_type,
                    project.current_stage,
                ]
            )

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="projects.xlsx"'
        wb.save(response)

        return response

        # return Response(serializer.data, status=200)


class AttachmentsViewSet(ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["uploaded_for", "uploaded_by"]

class RequiredAttachmentsViewSet(GenericAPIView):
    
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        required_attachments = project.required_attachments
        
        attachments = {}
        attachments_list = list(Attachment.objects.filter(uploaded_for=project))
        
        for attachment in attachments_list:
            if attachment.type not in attachments:
                attachments[attachment.type] = []
            attachments[attachment.type].insert(
                0, (attachment.attachment.url)
            )
        
        return Response({"required_attachments": required_attachments, "current_attachments": attachments}, status=200)
    
    def update(self, request, project_id):
        project = Project.objects.get(id=project_id)
        required_attachments = request.data.get('required_attachments')
        project.required_attachments = required_attachments
        project.save()
        return Response({"message": "Required attachments updated successfully"}, status=200)

class DashboardView(APIView):
    def get(self, request):
        total_projects = Project.objects.all().count()
        active_projects = Project.objects.filter(
            current_stage__in=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        ).count()
        completed_projects = Project.objects.filter(current_stage=13).count()
        inactive_projects = total_projects - (active_projects + completed_projects)

        return Response(
            {
                "total_projects": total_projects,
                "active_projects": active_projects,
                "completed_projects": completed_projects,
                "inactive_projects": inactive_projects,
            },
            status=200,
        )


class DelayedProjectsView(APIView):
    def get(self, request):
        sketch_projects = Project.objects.filter(current_stage=1).order_by("-moved_at")
        execution_stage_projects = Project.objects.filter(current_stage=4).order_by(
            "-moved_at"
        )

        result = {}

        result["sketch_projects"] = []
        for project in sketch_projects:
            days_since_moved = (
                (timezone.now() - project.moved_at).days if project.moved_at else None
            )

            result["sketch_projects"].append(
                {
                    "id": project.id,
                    "project_name": project.project_name,
                    "current_stage": project.current_stage,
                    "moved_at": project.moved_at,
                    "days_since_moved": days_since_moved,
                }
            )

        result["execution_stage_projects"] = []
        for project in execution_stage_projects:
            days_since_moved = (
                (timezone.now() - project.moved_at).days if project.moved_at else None
            )

            result["execution_stage_projects"].append(
                {
                    "id": project.id,
                    "project_name": project.project_name,
                    "current_stage": project.current_stage,
                    "moved_at": project.moved_at,
                    "days_since_moved": days_since_moved,
                }
            )

        return Response(result, status=200)


class CommentsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    filter_Backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["written_for"]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TableViewsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = TableView.objects.all()
    serializer_class = TableViewSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["employee", "stage", "name"]


# Learn Authentication
class HelloView(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {"message": "Hello World!"}
        return Response(content)


class BaladyProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = BaladyProject.objects.all()
    serializer_class = BaladyProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by("moved_at")
        return queryset

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        path = instance.path
        new_path = data.get("path")

        if data.get("path") == None:
            data["path"] = instance.path
        if data.get("project_name") == None:
            data["project_name"] = instance.project_name
        if data.get("request_type") == None:
            data["request_type"] = instance.request_type

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        if path != data.get("path"):
            instance.moved_at = timezone.now()
        instance.save()
        return Response(serializer.data)

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["path", "project_name", "client_phone"]


class LandSurveyProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = LandSurveyProject.objects.all()
    serializer_class = LandSurveyProjectSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["stage"]


class SortingDeedsProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = SortingDeedsProject.objects.all()
    serializer_class = SortingDeedsProjectSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["stage"]

class GlobalIDsViewSet(ModelViewSet):
    queryset = GlobalID.objects.all()
    serializer_class = GlobalIDSerializer