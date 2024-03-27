from django.urls import path
from .views import signin, signup, signout

# URLs' Account
urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
]