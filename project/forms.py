from django.forms import ModelForm, DateTimeInput
from .models import Project

# Create Form for app Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name_project',
            'category',
            'image',
            ]
        
""" Los campos de prueba despues se implementarán con funciones mas complejas"""