from django.contrib.auth import login
from django.utils import timezone
from django.contrib.auth.models import Group
from django.db.models import Count, Q, Func, IntegerField, Case, When, Value, F
from django.db.models.functions import Coalesce
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.core.mail import send_mail

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
    QatariOfficeProject,
    ReceptionProject,
    PasswordReset,
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
    MunicipalityVisitSerializer,
    QatariOfficeProjectSerializer,
    ProjectNameCheckSerializer,
    ReceptionProjectSerializer,
    ResetPasswordRequestSerializer,
)

# from .permissions import HasGroupPermission

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsAdmin
from .templates import ATTACHMENT_TEMPLATES


class JsonbArrayLength(Func):
    function = "jsonb_array_length"
    output_field = IntegerField()


# Projects Views
class ReceptionProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = ReceptionProject.objects.all()
    serializer_class = ReceptionProjectSerializer


class DesignProjectsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = DesignProject.objects.annotate(
        comments_count=Count("global_id__comments", distinct=True),
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

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        # if stage != data.get("stage"):
        #     instance.moved_at = timezone.now()
        #     if instance.s_history == None:
        #         instance.s_history = []
        #     instance.s_history.append(
        #         {
        #             "moved_by": str(self.request.user),
        #             "moved_at": str(timezone.now()),
        #             "from": stage,
        #             "to": new_stage,
        #         }
        #     )
        instance.save()
        return Response(serializer.data)

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["stage"]


class BaladyProjectsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    # TODO: check if the attachments types are included in the required_attachments
    queryset = BaladyProject.objects.annotate(
        comments_count=Count("global_id__comments", distinct=True),
        required_attachments_count=JsonbArrayLength("required_attachments"),
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

        if data.get("client_phone") == None:
            data["client_phone"] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get("client_phone"))

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        if stage != data.get("stage"):
            instance.moved_at = timezone.now()
        instance.save()
        return Response(serializer.data)

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["stage", "project_name", "client_phone"]


class LandSurveyProjectsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    # TODO: check if the attachments types are included in the required_attachments
    queryset = LandSurveyProject.objects.annotate(
        comments_count=Count("global_id__comments"),
        attachments_count=Count("global_id__attachments"),
        required_attachments_count=JsonbArrayLength("required_attachments"),
    )
    serializer_class = LandSurveyProjectSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        instance = self.get_object()

        stage = instance.stage
        new_stage = data.get("stage")

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
    permission_classes = (IsAuthenticated,)

    # TODO: check if the attachments types are included in the required_attachments
    queryset = SortingDeedsProject.objects.annotate(
        comments_count=Count("global_id__comments"),
        attachments_count=Count("global_id__attachments"),
        required_attachments_count=JsonbArrayLength("required_attachments"),
    )
    serializer_class = SortingDeedsProjectSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        # partial = kwargs.pop("partial", False)
        instance = self.get_object()

        stage = instance.stage
        new_stage = data.get("stage")

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


class QatariOfficeProjectsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    # TODO: check if the attachments types are included in the required_attachments
    queryset = QatariOfficeProject.objects.annotate(
        comments_count=Count("global_id__comments"),
        attachments_count=Count("global_id__attachments"),
        required_attachments_count=JsonbArrayLength("required_attachments"),
    )
    serializer_class = QatariOfficeProjectSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        instance = self.get_object()

        stage = instance.stage
        new_stage = data.get("stage")

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


# Projects Related Views
class ResetPasswordView(GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ResetPasswordRequestSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
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
                'aljarrashc@gmail.com',
                [email],
                fail_silently=False,
            )
            
            return Response({"sucess": "We have sent you an email. Please check your inbox."}, status=200)
        else:
            return Response({"error": "Employee not found"}, status=400)
    

class MoveProjectsViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data

        get_model_serializer = {
            "design": {"model": DesignProject, "serializer": DesignProjectSerializer},
            "balady": {"model": BaladyProject, "serializer": BaladyProjectSerializer},
            "sorting": {
                "model": SortingDeedsProject,
                "serializer": SortingDeedsProjectSerializer,
            },
            "land": {
                "model": LandSurveyProject,
                "serializer": LandSurveyProjectSerializer,
            },
        }

        from_model = get_model_serializer[data.get("from")]["model"]
        to_serializer = get_model_serializer[data.get("to")]["serializer"]

        origin_instance = from_model.objects.filter(id=data.get("id"))[0]
        params = {
            "project_name": origin_instance.project_name,
            "stage": "sketch",
            "client_phone": origin_instance.client_phone.phone,
            "project_type": "new",
            "use_type": "residential",
        }

        serializer = to_serializer(data=params, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"status": "Moved"}, status=200)


class TableViewsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = TableView.objects.all()
    serializer_class = TableViewSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["employee", "stage", "name"]


class ProjectNameCheckViewSet(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = ProjectNameCheckSerializer

    def get(self, request, project_category):
        data = request.query_params
        response = (
            ATTACHMENT_TEMPLATES[project_category]["model"]
            .objects.filter(project_name=data["project_name"])
            .exists()
        )

        return Response({"available": not response}, status=200)


# class HistoryViewSet(APIView):
#     permission_classes = (IsAuthenticated, )
#     def get(self, request, project_id):
#         project = DesignProject.objects.get(id=project_id)
#         return Response(project.s_history, status=200)


class RequiredAttachmentsViewSet(GenericAPIView):
    permission_classes = (IsAuthenticated,)

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
                attachments[attachment.type] = []
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
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated, IsAdmin)

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


class MunicipalityVisitsView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MunicipalityVisitSerializer

    def get(self, request, project_id):
        visits = BaladyProject.objects.get(id=project_id).municipality_visits
        return Response({"visits": visits}, 200)

    def put(self, request, project_id):
        data = request.data
        instance = BaladyProject.objects.get(id=project_id)
        instance.municipality_visits = data.get("visits")
        instance.save()

        return Response(instance.municipality_visits, 200)


class CopyBaladyProjectsView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ids = request.data.get("ids")
        stage = request.data.get("stage")

        if not ids or not stage:
            return Response({"message": "ids and stage are required"}, status=400)

        try:
            projects = BaladyProject.objects.filter(id__in=ids)
            new_projects = []
            for project in projects:
                project.id = None
                project.stage = stage
                # TODO: add s_history
                # project.created_at = timezone.now()
                project.moved_at = timezone.now()
                project.save()
                new_projects.append(project)

            serializer = BaladyProjectSerializer(new_projects, many=True)

            return Response(serializer.data, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=400)


class CopyProjectsView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, project_category):
        model_class = ATTACHMENT_TEMPLATES[project_category]["model"]
        ids = request.data.get("ids")
        stage = request.data.get("stage")
        

        if not ids or not stage:
            return Response({"message": "ids and stage are required"}, status=400)

        try:
            print(model_class.objects.filter(id__in=ids))
            return Response({"result": "Copied successfully"}, status=201)

        except Exception as e:
            raise e
            return Response({"error": e}, status=400)


class EngineersView(APIView):
    permission_classes = (IsAuthenticated,)

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

        design_projects = (
            DesignProject.objects.filter(stage="deleted_projects")
            .values("id", "global_id", "client_phone", "project_name")
            .annotate(category=Value("design"))
        )
        balady_projects = (
            BaladyProject.objects.filter(stage="deleted_projects")
            .values("id", "global_id", "client_phone", "project_name")
            .annotate(category=Value("balady"))
        )
        land_projects = (
            LandSurveyProject.objects.filter(stage="deleted_projects")
            .values("id", "global_id", "client_phone", "project_name")
            .annotate(category=Value("land_survey"))
        )
        sort_projects = (
            SortingDeedsProject.objects.filter(stage="deleted_projects")
            .values("id", "global_id", "client_phone", "project_name")
            .annotate(category=Value("sorting_deeds"))
        )
        qatari_projects = (
            QatariOfficeProject.objects.filter(stage="deleted_projects")
            .values("id", "global_id", "client_phone", "project_name")
            .annotate(category=Value("qatari"))
        )

        deleted_projects.extend(design_projects)
        deleted_projects.extend(balady_projects)
        deleted_projects.extend(land_projects)
        deleted_projects.extend(sort_projects)
        deleted_projects.extend(qatari_projects)

        return Response(deleted_projects, status=200)


# Auth Views
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
    permission_classes = (IsAuthenticated,)

    queryset = GlobalID.objects.all()
    serializer_class = GlobalIDSerializer


class CommentsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    filter_Backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["written_for"]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AttachmentsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["uploaded_for", "uploaded_by"]


class ClientsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class GroupsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EmployeesViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    def get(self, request):
        user = request.user
        data = {"isAdmin": user.is_superuser, "isStaff": user.is_staff}
        return Response(data)
