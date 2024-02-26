from django.forms import ModelForm
from .models import Project

# Create Form for app Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name_project', 'category', 'date_complete']