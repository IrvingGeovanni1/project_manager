"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import index
from account.views import signup, signin, signout
from project.views import project, create_project, project_detail, complete_project, delete_project
from task.views import task, create_task, task_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', signout, name='logout'),
    path('projects/', project, name='projects'),
    path("projects/<int:project_id>/", project_detail, name="project_detail"),
    path("projects/<int:project_id>/complete", complete_project, name='complete_project'),
    path("projects/<int:project_id>/delete", delete_project, name='delete_project'),
    path('projects/create_project/', create_project, name='create_project'),
    path('tasks/', task, name='tasks'),
    path('tasks/<int:task_id>', task_detail, name='task_detail'),
    path('tasks/create_task/', create_task, name='create_task'),
]
