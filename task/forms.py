from django.forms import ModelForm
from .models import Task

#Create Form for app Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project']