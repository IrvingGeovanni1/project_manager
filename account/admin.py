from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here - Custom UserAdmin
class UserAdmin(admin.ModelAdmin):
    readonly_fields = (
        'last_login',
        "date_joined",
        "updated_at",
        )
    
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'profile_picture',
        )

admin.site.register(User, UserAdmin)