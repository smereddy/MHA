from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser

class AppUserAdmin(UserAdmin):
   model = AppUser
   list_display = ['username', 'email', 'position', 'skillset', 'mobile_phone', 'work_phone', 'is_staff', 'is_superuser']
   list_filter = ['username', 'email', 'position', 'skillset', 'is_staff', 'is_superuser']
   fieldsets = (
         ('Account Information', {
            'fields': ('username', 'password', 'is_staff', 'is_superuser')
        }),
         ('Position', {
            'fields': ('position', 'skillset')
        }),
         ('Contact Information', {
            'fields': ('email', 'mobile_phone', 'work_phone')
        })
   )
   add_fieldsets = (
         ('Account Information', {
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser')
        }),
         ('Position', {
            'fields': ('position', 'skillset')
        }),
         ('Contact Information', {
            'fields': ('email', 'mobile_phone', 'work_phone')
        })
   )

admin.site.register(AppUser, AppUserAdmin)
