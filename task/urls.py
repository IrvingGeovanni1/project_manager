from django.urls import path
from .views import create_task, task, tasks_completed, task_detail, complete_task, uncomplete_task, delete_task

# URLs' Tasks
urlpatterns = [
    path('create_task/', create_task, name='create_task'),
    path('pending/', task, name='tasks'),
    path('completed/', tasks_completed, name='tasks_completed'),
    path('<int:task_id>/', task_detail, name='task_detail'),
    path('<int:task_id>/complete/', complete_task, name='complete_task'),
    path('<int:task_id>/uncomplete/', uncomplete_task, name='uncomplete_task'),
    path('<int:task_id>/delete', delete_task, name='delete_task'),
]
