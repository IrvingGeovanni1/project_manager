from django.contrib import admin
from .models import Task

# Create New Classes
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at"
    )

# Register your models here.
admin.site.register(Task, TaskAdmin)