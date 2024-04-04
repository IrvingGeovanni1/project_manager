from rest_framework import viewsets
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer
from account.models import User
from project.models import Project
from task.models import Task

# Create ViewSets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSer(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer