from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserModel


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserModel
    list_display = [
        'email',
        'username',
        'is_staff',
        'about',
        'photo',
        'name',
        'family',
        'is_shopper',
    ]

    fieldsets = UserAdmin.fieldsets + \
        ((None, {"fields": ('name', 'photo','family','is_shopper','about')}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
        ((None, {"fields": ('name', 'photo','family','is_shopper','about')}),)


admin.site.register(UserModel, CustomUserAdmin)