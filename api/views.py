from django.contrib.auth import login
from django.utils import timezone
from django.contrib.auth.models import Group
from django.db.models import Count, Q, Func, IntegerField, Case, When, Value, F
from django.db.models.functions import Coalesce
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from urllib.parse import unquote

from django.core.mail import send_mail

import io
import zipfile
import requests
from django.http import HttpResponse

import os

# from django.db.models.functions import JSONObject

from .models import (
    Employee,
    Client,
    DesignProject,
    Attachment,
    Comment,
    TableView,
    BaladyProject,
    LandSurveyProject,
    SortingDeedsProject,
    GlobalID,
    QatariProject,
    ReceptionProject,
    PasswordReset,
    SupervisionProject,
    Visit,
    History,
)
from .serializers import (
    EmployeeSerializer,
    RemoveTokensSerializer,
    ClientSerializer,
    DesignProjectSerializer,
    AttachmentSerializer,
    RequiredAttachmentSerializer,
    PaymentsSerializer,
    CommentSerializer,
    TableViewSerializer,
    BaladyProjectSerializer,
    LandSurveyProjectSerializer,
    SortingDeedsProjectSerializer,
    GlobalIDSerializer,
    GroupSerializer,
    RequestSubmissionSerializer,
    CopyProjectsSerializer,
    QatariProjectSerializer,
    ProjectNameCheckSerializer,
    ReceptionProjectSerializer,
    ResetPasswordRequestSerializer,
    SupervisionProjectSerializer,
    VisitSerializer,
    HistorySerializer,
)

# from .permissions import HasGroupPermission

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from django_filters.rest_framework import DjangoFilterBackend

# from .permissions import IsAdmin
from .templates import ATTACHMENT_TEMPLATES


class JsonbArrayLength(Func):
    function = "jsonb_array_length"
    output_field = IntegerField()


# Projects Views
class ReceptionProjectsViewSet(ModelViewSet):

    queryset = ReceptionProject.objects.annotate(
        comments_count=Count("global_id__comments", distinct=True),
        category=Value("reception"),
    )
    serializer_class = ReceptionProjectSerializer


class DesignProjectsViewSet(ModelViewSet):

    queryset = DesignProject.objects.annotate(
        comments_count=Count("global_id__comments", distinct=True),
        category=Value("design"),
        # attachments_count=Count(
        #     "global_id__attachments__type",
        #     filter=~Q(global_id__attachments__type="other"),
        #     distinct=True,
        # ),
        # required_attachments_count=JsonbArrayLength("required_attachments"),
    )
    serializer_class = DesignProjectSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        # partial = kwargs.pop("partial", False)
        instance = self.get_object()

        stage = instance.stage
        new_stage = data.get("stage")

        if new_stage != stage:
            instance.moved_at = timezone.now()
            if new_stage == "deleted_projects":
                instance.delete_stage = stage
            else:
                instance.delete_stage = None

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        instance.save()
        return Response(serializer.data)

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["stage"]


class BaladyProjectsViewSet(ModelViewSet):

    # TODO: check if the attachments types are included in the required_attachments
    queryset = BaladyProject.objects.annotate(
        comments_count=Count("global_id__comments", distinct=True),
        visits_count=Count("global_id__visits", distinct=True),
        required_attachments_count=JsonbArrayLength("required_attachments"),
        category=Value("balady"),
        attachments_count=Coalesce(
            Case(
                When(required_attachments_count=0, then=Value(0)),
                default=(
                    Count(
                        "global_id__attachments__type",
                        filter=~Q(global_id__attachments__type="other"),
                        distinct=True,
                    )
                    * 3
                )
                / F("required_attachments_count"),
                output_field=IntegerField(),
            ),
            0,
            output_field=IntegerField(),
        ),
    )
    serializer_class = BaladyProjectSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        # partial = kwargs.pop("partial", False)
        instance = self.get_object()

        stage = instance.stage
        new_stage = data.get("stage")

        if new_stage != stage:
            instance.moved_at = timezone.now()
            if new_stage == "deleted_projects":
                instance.delete_stage = stage
            else:
                instance.delete_stage = None

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        instance.save()
        return Response(serializer.data)

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["stage", "project_name", "client_phone"]


class LandSurveyProjectsViewSet(ModelViewSet):

    # TODO: check if the attachments types are included in the required_attachments
    queryset = LandSurveyProject.objects.annotate(
        comments_count=Count("global_id__comments"),
        attachments_count=Count("global_id__attachments"),
        category=Value("land_survey"),
        required_attachments_count=JsonbArrayLength("required_attachments"),
    )
    serializer_class = LandSurveyProjectSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        instance = self.get_object()

        stage = instance.stage
        new_stage = data.get("stage")

        if new_stage != stage:
            instance.moved_at = timezone.now()
            if new_stage == "deleted_projects":
                instance.delete_stage = stage
            else:
                instance.delete_stage = None

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        instance.save()
        return Response(serializer.data)

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["stage"]


class SortingDeedsProjectsViewSet(ModelViewSet):

    # TODO: check if the attachments types are included in the required_attachments
    queryset = SortingDeedsProject.objects.annotate(
        comments_count=Count("global_id__comments"),
        attachments_count=Count("global_id__attachments"),
        category=Value("sorting_deeds"),
        required_attachments_count=JsonbArrayLength("required_attachments"),
    )
    serializer_class = SortingDeedsProjectSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        # partial = kwargs.pop("partial", False)
        instance = self.get_object()

        stage = instance.stage
        new_stage = data.get("stage")

        if new_stage != stage:
            instance.moved_at = timezone.now()
            if new_stage == "deleted_projects":
                instance.delete_stage = stage
            else:
                instance.delete_stage = None

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        instance.save()
        return Response(serializer.data)

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["stage"]


class QatariProjectsViewSet(ModelViewSet):

    # TODO: check if the attachments types are included in the required_attachments
    queryset = QatariProject.objects.annotate(
        comments_count=Count("global_id__comments"),
        attachments_count=Count("global_id__attachments"),
        category=Value("qatari"),
        required_attachments_count=JsonbArrayLength("required_attachments"),
    )
    serializer_class = QatariProjectSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        instance = self.get_object()

        stage = instance.stage
        new_stage = data.get("stage")

        if new_stage != stage:
            instance.moved_at = timezone.now()
            if new_stage == "deleted_projects":
                instance.delete_stage = stage
            else:
                instance.delete_stage = None

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        instance.save()
        return Response(serializer.data)

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["stage"]


class SupervisionProjectsViewSet(ModelViewSet):

    queryset = SupervisionProject.objects.annotate(
        comments_count=Count("global_id__comments", distinct=True),
        category=Value("supervision"),
        visits_count=Count("global_id__visits", distinct=True),
    )
    serializer_class = SupervisionProjectSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        instance = self.get_object()

        stage = instance.stage
        new_stage = data.get("stage")

        if new_stage != stage:
            instance.moved_at = timezone.now()
            if new_stage == "deleted_projects":
                instance.delete_stage = stage
            else:
                instance.delete_stage = None

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        instance.save()
        return Response(serializer.data)

    filter_Backends = [DjangoFilterBackend]
    filterset_fields = ["stage"]


# Projects Related Views
class CompressFilesView(APIView):
    def post(self, request, *args, **kwargs):
        # List of file URLs sent from the client
        file_urls = request.data.get('file_urls', [])
        
        # Create an in-memory zip file
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for url in file_urls:
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        # Get the file name from the URL
                        filename = unquote(url.split("/")[-1].split("?")[0])
                        # Write the file content to the zip
                        zip_file.writestr(filename, response.content)
                except Exception as e:
                    # Handle exception if the file cannot be downloaded
                    print(f"Error downloading {url}: {e}")
                    continue
        
        # Set the pointer to the beginning of the stream
        zip_buffer.seek(0)
        
        # Create an HTTP response with the zip file
        response = HttpResponse(zip_buffer, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=compressed_files.zip'
        
        return response
    

class CopyProjectsView(GenericAPIView):
    serializer_class = CopyProjectsSerializer
    model_name_serializer = {
        "reception": ReceptionProjectSerializer,
        "design": DesignProjectSerializer,
        "balady": BaladyProjectSerializer,
        "land_survey": LandSurveyProjectSerializer,
        "sorting_deeds": SortingDeedsProjectSerializer,
        "qatari": QatariProjectSerializer,
        "supervision": SupervisionProjectSerializer,
    }

    def post(self, request, project_category):
        data = request.data
        ser = self.get_serializer(data=data)
        ser.is_valid(raise_exception=True)
        src_model = ATTACHMENT_TEMPLATES[project_category]["model"]
        # dest_model = ATTACHMENT_TEMPLATES[data["target_category"]]["model"]
        

        dest_serializer = self.model_name_serializer[data["target_category"]]
        
        
        for id in ser.data["ids"]:
            project = src_model.objects.get(id=id)
            project.id = None
            old_global_id = project.global_id
            project.global_id = None
            project.stage = data.get("target_stage")
            
            project.request_types = data.get("request_types", None)
            project.project_type = data.get("project_type", None)
            project.use_type = data.get("use_type", None)
            
            temp = dest_serializer(project)
            dest_ser = dest_serializer(
                data=temp.data,
            )
            dest_ser.is_valid(raise_exception=True)
            dest_ser.save()
            
            if data.get("comments_included", False):
                for comment in old_global_id.comments.all():
                    # comment.global_id = dest_ser.instance.global_id
                    # comment.save()
                    Comment.objects.create(content=comment.content, written_for=dest_ser.instance.global_id, written_by=comment.written_by)


        return Response({"category": project_category}, status=200)


class HistoryViewSet(ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project", "user", "action"]


class VisitsViewSet(ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["visited_for"]


class ResetPasswordView(GenericAPIView):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data["email"]
        employee = Employee.objects.filter(email=email).first()

        if employee:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(employee)
            reset = PasswordReset(email=email, token=token)
            reset.save()

            reset_url = f"{os.environ.get('FRONTEND_URL')}/reset-password/{token}"

            send_mail(
                "Password Reset",
                f"You can reset your password here: {reset_url}",
                "aljarrashc@gmail.com",
                [email],
                fail_silently=False,
            )

            return Response(
                {"sucess": "We have sent you an email. Please check your inbox."},
                status=200,
            )
        else:
            return Response({"error": "Employee not found"}, status=400)


class TableViewsViewSet(ModelViewSet):

    queryset = TableView.objects.all()
    serializer_class = TableViewSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["employee", "stage", "name"]


class ProjectNameCheckViewSet(GenericAPIView):

    serializer_class = ProjectNameCheckSerializer

    def get(self, request, project_category):
        project_name = request.query_params["project_name"]
        if ReceptionProject.objects.filter(project_name=project_name).exists():
            return Response({"available": False, "category": "reception"}, status=200)
        elif DesignProject.objects.filter(project_name=project_name).exists():
            return Response({"available": False, "category": "design"}, status=200)
        elif BaladyProject.objects.filter(project_name=project_name).exists():
            return Response({"available": False, "category": "balady"}, status=200)
        elif LandSurveyProject.objects.filter(project_name=project_name).exists():
            return Response({"available": False, "category": "land_survey"}, status=200)
        elif SortingDeedsProject.objects.filter(project_name=project_name).exists():
            return Response(
                {"available": False, "category": "sorting_deeds"}, status=200
            )
        elif QatariProject.objects.filter(project_name=project_name).exists():
            return Response({"available": False, "category": "qatari"}, status=200)
        elif SupervisionProject.objects.filter(project_name=project_name).exists():
            return Response({"available": False, "category": "supervision"}, status=200)
        # response = (
        #     ATTACHMENT_TEMPLATES[project_category]["model"]
        #     .objects.filter(project_name=data["project_name"])
        #     .exists()
        # )

        return Response({"available": True}, status=200)


class RequiredAttachmentsViewSet(GenericAPIView):

    serializer_class = RequiredAttachmentSerializer

    def get(self, request, project_category, project_id):
        attachment_template = ATTACHMENT_TEMPLATES[project_category]
        instance = attachment_template["model"].objects.get(id=project_id)
        required_attachments = instance.required_attachments

        constants = attachment_template.get(
            "constants",
        )
        for index, required_attachment in enumerate(required_attachments):
            if required_attachment in constants["type_1"]:
                required_attachments[index] = f"1_{required_attachments[index]}"
            elif required_attachment in constants["type_2"]:
                required_attachments[index] = f"2_{required_attachments[index]}"
            elif required_attachment in constants["type_3"]:
                required_attachments[index] = f"3_{required_attachments[index]}"

        attachments = {}
        attachments_list = list(
            Attachment.objects.filter(uploaded_for=instance.global_id)
        )

        for attachment in attachments_list:
            if attachment.type not in attachments:
                if attachment.type == "other":
                    attachments[attachment.type] = {"links": [], "notes": []}
                else:
                    attachments[attachment.type] = []
            if attachment.type == "other":
                attachments["other"]["links"].insert(
                    0, (f"{attachment.id}_{attachment.attachment.url}")
                )
                attachments["other"]["notes"].insert(0, attachment.note)
            else:
                attachments[attachment.type].insert(
                    0, (f"{attachment.id}_{attachment.attachment.url}")
                )

        return Response(
            {
                "required_attachments": required_attachments,
                "current_attachments": attachments,
            },
            status=200,
        )

    def put(self, request, project_category, project_id):
        attachment_template = ATTACHMENT_TEMPLATES[project_category]
        instance = attachment_template["model"].objects.get(id=project_id)
        required_attachments = request.data.get("required_attachments")
        instance.required_attachments = required_attachments
        instance.save()

        attachments = {}
        attachments_list = list(
            Attachment.objects.filter(uploaded_for=instance.global_id)
        )

        for attachment in attachments_list:
            if attachment.type not in attachments:
                attachments[attachment.type] = []
            attachments[attachment.type].insert(0, (attachment.attachment.url))

        return Response(
            {
                "required_attachments": required_attachments,
                "current_attachments": attachments,
            },
            status=200,
        )


class RequestSubmissionsView(GenericAPIView):
    serializer_class = RequestSubmissionSerializer

    def get(self, request, project_id):
        requests = BaladyProject.objects.get(id=project_id).request_submissions
        return Response({"requests": requests}, 200)

    def put(self, request, project_id):
        data = request.data
        instance = BaladyProject.objects.get(id=project_id)
        instance.request_submissions = data.get("requests")
        instance.save()

        return Response(instance.request_submissions, 200)


class PaymentsViewSet(GenericAPIView):
    permission_classes = (IsAdminUser,)

    serializer_class = PaymentsSerializer

    def get(self, request, project_category, project_id):
        attachment_template = ATTACHMENT_TEMPLATES[project_category]
        instance = attachment_template["model"].objects.get(id=project_id)

        attachments = []
        contracts = list(
            Attachment.objects.filter(uploaded_for=instance.global_id, type="contract")
        )

        for contract in contracts:
            attachments.insert(0, (f"{contract.id}_{contract.attachment.url}"))

        return Response(
            {
                "s_contract": list(attachments),
                "s_project_value": instance.s_project_value,
                "s_payments": instance.s_payments,
            },
            status=200,
        )

    def put(self, request, project_category, project_id):
        attachment_template = ATTACHMENT_TEMPLATES[project_category]
        instance = attachment_template["model"].objects.get(id=project_id)
        data = request.data

        instance.s_project_value = data.get("s_project_value")
        instance.s_payments = data.get("s_payments")

        instance.save()

        return Response(
            {
                "s_project_value": instance.s_project_value,
                "s_payments": instance.s_payments,
            },
            status=200,
        )


class EngineersView(APIView):

    def get(self, request):
        groups = Group.objects.all()
        ids = {}
        response = {}
        for group in groups:
            Employee.objects.filter(groups=group)
            array = Employee.objects.filter(groups=group).values("id", "username")
            employee_dict = {employee["id"]: employee["username"] for employee in array}
            ids = {**ids, **employee_dict}
            response[group.name] = array

        response["ids"] = ids
        return Response(response)


class DeletedProjectsView(APIView):

    def get(self, request):
        deleted_projects = []

        design_projects = list(
            DesignProject.objects.filter(stage="deleted_projects")
            .values(
                "id",
                "global_id",
                "client_phone",
                "project_name",
                "delete_stage",
                "moved_at",
            )
            .annotate(category=Value("design"), comments_count=Count("global_id__comments"))
        )
        balady_projects = list(
            BaladyProject.objects.filter(stage="deleted_projects")
            .values(
                "id",
                "global_id",
                "client_phone",
                "project_name",
                "delete_stage",
                "moved_at",
            )
            .annotate(category=Value("balady"), comments_count=Count("global_id__comments"))
        )
        land_projects = list(
            LandSurveyProject.objects.filter(stage="deleted_projects")
            .values(
                "id",
                "global_id",
                "client_phone",
                "project_name",
                "delete_stage",
                "moved_at",
            )
            .annotate(category=Value("land_survey"), comments_count=Count("global_id__comments"))
        )
        sort_projects = list(
            SortingDeedsProject.objects.filter(stage="deleted_projects")
            .values(
                "id",
                "global_id",
                "client_phone",
                "project_name",
                "delete_stage",
                "moved_at",
            )
            .annotate(category=Value("sorting_deeds"), comments_count=Count("global_id__comments"))
        )
        qatari_projects = list(
            QatariProject.objects.filter(stage="deleted_projects")
            .values(
                "id",
                "global_id",
                "client_phone",
                "project_name",
                "delete_stage",
                "moved_at",
            )
            .annotate(category=Value("qatari"), comments_count=Count("global_id__comments"))
        )
        supervision_projects = list(
            SupervisionProject.objects.filter(stage="deleted_projects")
            .values(
                "id",
                "global_id",
                "client_phone",
                "project_name",
                "delete_stage",
                "moved_at",
            )
            .annotate(category=Value("supervision"), comments_count=Count("global_id__comments"))
        )

        deleted_projects = (
            design_projects
            + balady_projects
            + land_projects
            + sort_projects
            + qatari_projects
            + supervision_projects
        )

        return Response(deleted_projects, status=200)


# Auth Views
class RemoveTokensAPI(GenericAPIView):

    serializer_class = RemoveTokensSerializer

    def post(self, request, format=None):
        if not request.user.is_staff:
            return Response(
                {"message": "You are not authorized to perform this action"}, status=403
            )
        user = Employee.objects.get(username=request.data["username"])
        AuthToken.objects.filter(user=user).delete()
        return Response({"message": "Tokens removed successfully"})


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


# Other Views
class GlobalIDsViewSet(ModelViewSet):

    queryset = GlobalID.objects.all()
    serializer_class = GlobalIDSerializer


class CommentsViewSet(ModelViewSet):

    filter_Backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["written_for"]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AttachmentsViewSet(ModelViewSet):

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["uploaded_for", "uploaded_by"]


class ClientsViewSet(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class GroupsViewSet(ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EmployeesViewSet(ModelViewSet):

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

        if data.get("username") == None:
            data["username"] = instance.username

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.save()

        return Response(serializer.data)


class EmployeeRolesViewSet(APIView):

    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    def get(self, request):
        user = request.user
        data = {"isAdmin": user.is_superuser, "isStaff": user.is_staff}
        return Response(data)
