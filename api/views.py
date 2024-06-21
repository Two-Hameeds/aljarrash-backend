from django.forms.models import model_to_dict
from django.contrib.auth import login
from django.utils import timezone

from .models import Employee, Client, Project, Attachment, Comment, TableView, UseTypes, BaladyProject, LandSurveyProject
from .serializers import EmployeeSerializer, RegisterSerializer, RemoveTokensSerializer, ClientSerializer, ProjectSerializer, AttachmentSerializer, CommentSerializer, TableViewSerializer, BaladyProjectSerializer, LandSurveyProjectSerializer
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


class EmployeesViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        request.data['username'] = request.data['username'].lower().strip()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.save()
        
        return Response({"employee": EmployeeSerializer(employee, context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(employee)[1]
                         })
    

class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)
    
    def post(self, request, format=None):
        request.data['username'] = request.data['username'].lower().strip()
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.validated_data['user']
        login(request, employee)
        response = super(LoginAPI, self).post(request, format=None)
        if(response.status_code == 200):
            response.data["is_staff"] = employee.is_staff
        return response
    
class RemoveTokensAPI(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = RemoveTokensSerializer

    def post(self, request, format=None):
        if(not request.user.is_staff):
            return Response({"message": "You are not authorized to perform this action"}, status=403)
        user = Employee.objects.get(username=request.data['username'])
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
        queryset = queryset.order_by('moved_at')
        return queryset
    
    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        current_stage = instance.current_stage
        new_stage = data.get('current_stage')

        if(data.get('current_stage') == None):
            data['current_stage'] = instance.current_stage
        if(data.get('project_name') == None):
            data['project_name'] = instance.project_name
        if(data.get('project_type') == None):
            data['project_type'] = instance.project_type
        if(data.get('use_type') == None):
            data['use_type'] = instance.use_type
            
        if(data.get('client_phone') == None):
            data['client_phone'] = instance.client_phone.phone
        else:
            Client.objects.get_or_create(phone=data.get('client_phone'))
            # data['client_phone'] = client.phone
        

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        if(current_stage != new_stage):
            instance.moved_at = timezone.now()
        instance.save()
        return Response(serializer.data)

    
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['current_stage']
    
    
class CopyProjectsView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        stage = request.data.get('stage')
        
        if not ids or not stage:
            return Response({'message': 'ids and stage are required'}, status=400)
        
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
            return Response({'error': str(e)}, status=400)

class AttachmentsViewSet(ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['uploaded_for', 'uploaded_by']

class DashboardView(APIView):
    def get(self, request):
        total_projects = Project.objects.all().count()
        active_projects = Project.objects.filter(current_stage__in=[1,2,3,4,5,6,7,8,9,10,11,12]).count()
        completed_projects = Project.objects.filter(current_stage=13).count()
        inactive_projects = total_projects - (active_projects + completed_projects)
        
        return Response({'total_projects': total_projects, 'active_projects': active_projects, 'completed_projects': completed_projects, 'inactive_projects': inactive_projects}, status=200)

class DelayedProjectsView(APIView):
    def get(self, request):
        sketch_projects = Project.objects.filter(current_stage=1).order_by('-moved_at')
        execution_stage_projects = Project.objects.filter(current_stage=4).order_by('-moved_at')
        
        result = {}
        
        result['sketch_projects'] = []
        for project in sketch_projects:
            days_since_moved = (timezone.now() - project.moved_at).days if project.moved_at else None

            result['sketch_projects'].append({
                'id': project.id,
                'project_name': project.project_name,
                'current_stage': project.current_stage,
                'moved_at': project.moved_at,
                'days_since_moved': days_since_moved
            })
        
        result['execution_stage_projects'] = []
        for project in execution_stage_projects:
            days_since_moved = (timezone.now() - project.moved_at).days if project.moved_at else None
            
            result['execution_stage_projects'].append({
                'id': project.id,
                'project_name': project.project_name,
                'current_stage': project.current_stage,
                'moved_at': project.moved_at,
                'days_since_moved': days_since_moved
            })  
                    
        return Response(result, status=200)

class CommentsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    
    filter_Backends = [DjangoFilterBackend, ]
    filterset_fields = ['written_for']
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class TableViewsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    
    queryset = TableView.objects.all()
    serializer_class = TableViewSerializer
    
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['employee', 'stage', 'name']
    

# Learn Authentication
class HelloView(APIView):
    # permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        content = {'message': 'Hello World!'}
        return Response(content)

    
class BaladyProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    
    queryset = BaladyProject.objects.all()
    serializer_class = BaladyProjectSerializer
    
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['stage', 'request_status', 'project_type', 'architecture_status', 'construction_status', 'plumbing_status', 'electrical_status']

class LandSurveyProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    
    queryset = LandSurveyProject.objects.all()
    serializer_class = LandSurveyProjectSerializer
    
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['stage', 'location_visit', 'project_type', 'payment_status']