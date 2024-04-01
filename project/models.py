from django.db import models
from account.models import User

# Create your models here.

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name_project = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    date_completed = models.DateTimeField(null = True, blank=True)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Show Project name
    def __str__(self):
        return self.name_project