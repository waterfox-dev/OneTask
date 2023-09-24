from rest_framework import serializers
from OneTask.models import Task
from OneTask.models import Todo

class TodoSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Todo
        fields = ('tl_id', 'tl_title', 'tl_description')

class TaskSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Task
        fields = ('ta_id', 'ta_title', 'ta_description', 'ta_check', 'ta_todo')