from django.urls import path
from .views import profile, update_profile, signin, signup, signout

# URLs' Account
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
]