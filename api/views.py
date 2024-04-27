from .models import Employee, Client, Project, Comment, TableView
from .serializers import EmployeeSerializer, RegisterSerializer, ClientSerializer, ProjectSerializer, CommentSerializer, TableViewSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from knox.models import AuthToken

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
    

class CommentsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    
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