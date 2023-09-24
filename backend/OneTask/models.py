from django.db.models import Model 
from django.db.models import fields
from django.db.models import ForeignKey
from django.db.models import CASCADE


class Todo(Model) : 
    
    tl_id = fields.IntegerField(primary_key=True)
    tl_title = fields.CharField(max_length=64)
    tl_description = fields.TextField(blank=True, null=True)
    
    def __str__(self) -> str : 
        return f'{self.tl_id} - {self.tl_title}'

class Task(Model) : 
    
    ta_id = fields.IntegerField(primary_key=True)
    ta_title = fields.CharField(max_length=256)
    ta_description = fields.TextField(blank=True, null=True)
    ta_check = fields.BooleanField(default=False)
    
    ta_todo = ForeignKey(Todo, on_delete=CASCADE)

    def __str__(self) -> str :
        return f'{self.ta_id} - {self.ta_title}'