from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    id = models.CharField(primary_key=True, blank=True)
    type_user = models.CharField(max_lenght=50)
    update_at = models.DateTimeField(auto_now=True)