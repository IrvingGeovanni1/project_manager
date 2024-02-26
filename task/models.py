from django.db import models
from project.models import Project

# Create your models here.

class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    title = models.CharField(max_field=100)
    descripcion = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    id_projectr = models.ForeignKey(Project,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    