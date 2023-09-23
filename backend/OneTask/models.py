from django.db.models import Model 
from django.db.models import fields
from django.db.models import ForeignKey
from django.db.models import CASCADE


class TodoList(Model) : 
    
    tl_id = fields.IntegerField(primary_key=True)
    tl_title = fields.CharField(max_length=64)

class Task(Model) : 
    
    ta_id = fields.IntegerField(primary_key=True)
    ta_title = fields.CharField(max_length=256)
    ta_description = fields.TextField(blank=True, null=True)
    ta_check = fields.BooleanField(default=False)
    
    ta_list = ForeignKey(TodoList, on_delete=CASCADE)

