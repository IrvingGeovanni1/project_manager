from django.contrib import admin
from .models import Project

# Create New Classes
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "update_at",
        )

# Register your models here.
admin.site.register(Project, ProjectAdmin)
