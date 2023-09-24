from django.contrib import admin

from OneTask.models import Task
from OneTask.models import Todo

# Register your models here.
class TaskAdmin(admin.ModelAdmin) :
    list_display = ('ta_id', 'ta_title', 'ta_check')
    
class TodoAdmin(admin.ModelAdmin) :
    list_display = ('tl_id', 'tl_title')
    
admin.site.register(Task, TaskAdmin)
admin.site.register(Todo, TodoAdmin)