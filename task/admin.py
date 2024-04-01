from django.contrib import admin
from .models import Task

# Create New Classes
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = (
        'date_completed',
        "created_at",
        "updated_at"
    )

    list_display = (
        'title',
        'date_completed',
        'project',
    )

# Register your models here.
admin.site.register(Task, TaskAdmin)