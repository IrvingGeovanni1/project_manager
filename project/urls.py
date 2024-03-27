from django.urls import path
from .views import create_project, project, projects_completed, project_detail, complete_project, uncomplete_project, delete_project

# URLs' Project
urlpatterns = [
    path('create_project', create_project, name='create_project'),
    path('pending/', project, name='projects'),
    path('completed', projects_completed, name='projects_completed'),
    path('<int:project_id>', project_detail, name='project_detail'),
    path('<int:project_id>/complete', complete_project, name='complete_project'),
    path('<int:project_id>/uncomplete', uncomplete_project, name='uncomplete_project'),
    path('<int:project_id>/delete', delete_project, name='delete_project'),
]