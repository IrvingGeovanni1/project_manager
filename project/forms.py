from django.forms import ModelForm, DateInput
from .models import Project

# Create Form for app Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name_project', 'category', 'date_complete']
        # Create Form date type
        widgets = {
            'date_complete': DateInput(attrs={'type': 'date'}),
        }