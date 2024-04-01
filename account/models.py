from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    Type_choices = [
        ('free', 'Free'),
        ('premium', 'Premium'),
    ]

    profile_picture = models.ImageField(upload_to='portfolio/images/', blank=True)
    type_user = models.CharField(max_length=50, choices=Type_choices, default='free')
    updated_at = models.DateTimeField(auto_now=True)

    # Show User by Username
    def __str__(self):
        return self.username