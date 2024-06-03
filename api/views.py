from django.forms.models import model_to_dict
from django.contrib.auth import login
from django.utils import timezone

from .models import Employee, Client, Project, Comment, TableView
from .serializers import EmployeeSerializer, RegisterSerializer, ClientSerializer, ProjectSerializer, CommentSerializer, TableViewSerializer
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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.save()
        
        return Response({"employee": EmployeeSerializer(employee, context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(employee)[1]
                         })
    

class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.validated_data['user']
        login(request, employee)
        return super(LoginAPI, self).post(request, format=None)
    

class ClientsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    

class ProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['stage']
    
    def put(self, request, pk):
        try:
            obj = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response(status=404)
        
        serializer = ProjectSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
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
                project.stage = stage
                project.created_at = timezone.now()
                project.save()
                new_projects.append(project)
            
            serializer = ProjectSerializer(new_projects, many=True)

            return Response(serializer.data, status=201)
            
            
        except Exception as e:
            return Response({'error': str(e)}, status=400)

class DashboardView(APIView):
    def get(self, request):
        total_projects = Project.objects.all().count()
        active_projects = Project.objects.filter(stage__in=[1,2,3,4,5,6,7,8,9,10,11,12]).count()
        completed_projects = Project.objects.filter(stage=13).count()
        inactive_projects = total_projects - (active_projects + completed_projects)
        
        return Response({'total_projects': total_projects, 'active_projects': active_projects, 'completed_projects': completed_projects, 'inactive_projects': inactive_projects}, status=200)

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
    filterset_fields = ['employee', 'stage']
    

# Learn Authentication
class HelloView(APIView):
    # permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        content = {'message': 'Hello World!'}
        return Response(content)