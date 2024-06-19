from django import forms
from .models import Post , comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'photo']

class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['body']