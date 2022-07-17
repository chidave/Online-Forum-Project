from django.contrib import admin
from django.forms import Textarea
from .models import AppUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'first_name')
    list_display = ('email', 'username', 'first_name', 'is_active', 'is_staff', 'created_date')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'created_date')
    order = ('-created_date')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Personal', {'fields': ('about', )})
    )

    formfield_overrides = {
        AppUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})}
    }

    add_fieldsets = (
        (
            None, {
                'classes': ('wide', ),
                'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')
            }
        ),
    )

# Register your models here.
admin.site.register(AppUser, UserAdminConfig)