from django.db import models
from account.models import User

# Create your models here.

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name_project = models.CharField(max_lenght=100)
    category = models.CharField(max_lenght=50)
    complete = models.BooleanField(default=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    