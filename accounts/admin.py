from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, UserProfile

# Model Admin Customization
class customUserAdmin(UserAdmin):
    list_display = ['user_name', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff']
    ordering = ['user_name']
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'user_name', 'email', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )


# User Profile Admin Customization
class customUserProfile(admin.ModelAdmin):
    ordering = ['user']


# Register your models here.
admin.site.register(User, customUserAdmin)
admin.site.register(UserProfile, customUserProfile)
