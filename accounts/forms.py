from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserModel
        fields = UserCreationForm.Meta.fields + \
            ('name', 'photo','family','about')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = UserChangeForm.Meta.fields