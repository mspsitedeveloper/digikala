from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'is_staff',
        'about',
        'photo',
        'first_name',
        'last_name',
    ]

    fieldsets = UserAdmin.fieldsets + \
        ((None, {"fields": ('about', 'photo')}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
        ((None, {"fields": ('about', 'photo')}),)


admin.site.register(CustomUser, CustomUserAdmin)