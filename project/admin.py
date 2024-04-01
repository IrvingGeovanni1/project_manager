from django.contrib import admin
from .models import Project

# Create New Classes
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = (
        'date_completed',
        "created_at",
        "updated_at",
        )

    list_display = (
        'name_project',
        'category',
        'date_completed',
        'image',
    )
# Register your models here.
admin.site.register(Project, ProjectAdmin)
