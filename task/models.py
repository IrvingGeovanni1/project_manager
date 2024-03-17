from django.db import models
from project.models import Project

# Create your models here.

class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    #complete = models.BooleanField(default=False)
    date_complete = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Show title
    def __str__(self):
        return self.title + ' - ' + self.project.name_project