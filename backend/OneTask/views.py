from django.shortcuts import render

from rest_framework import viewsets

from OneTask.serializers import TodoSerializer
from OneTask.serializers import TaskSerializer

from OneTask.models import Todo 
from OneTask.models import Task 


class TodoView(viewsets.ModelViewSet) : 
    serializer_class = TodoSerializer 
    queryset = Todo.objects.all()
    
class TaskView(viewsets.ModelViewSet) : 
    serializer_class = TaskSerializer 
    queryset = Task.objects.all()