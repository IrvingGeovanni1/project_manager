from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    type_user = models.CharField(max_length=50)
    update_at = models.DateTimeField(auto_now=True)