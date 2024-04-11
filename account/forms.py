from django.forms import ModelForm
from .models import User

# Create Form for the User app

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'profile_picture',
        ]