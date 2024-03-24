from django.forms import ModelForm
from .models import Task
from project.models import Project

#Create Form for app Task

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['project'].queryset = Project.objects.filter(user=user)

    class Meta:
        model = Task
        fields = ['title',
                  'description',
                  'project'
                  ]