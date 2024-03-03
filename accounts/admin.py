from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User

# Model Admin Customization
class customUserAdmin(UserAdmin):
    list_display = ['user_name', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff']
    ordering = ['user_name']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



# Register your models here.
admin.site.register(User, customUserAdmin)
