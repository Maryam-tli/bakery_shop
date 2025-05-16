from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'email', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone_number', 'profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'profile_image', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
