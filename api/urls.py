from django.urls import path, include
from rest_framework import routers
from api import views

# Creating the router
router_user = routers.DefaultRouter()
router_user.register(r'users', views.UserViewSet)

router_project = routers.DefaultRouter()
router_project.register(r'projects', views.ProjectViewSet)

router_task = routers.DefaultRouter()
router_task.register(r'tasks', views.TaskViewSer)

# Declaring navigation routes
urlpatterns = [
    path('', include(router_user.urls)),
    path('', include(router_project.urls)),
    path('', include(router_task.urls)),
]