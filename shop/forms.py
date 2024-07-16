from django import forms
from .models import Product , Commentshop

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', "Price", 'photo', 'slug', 'desc']

class Comment_Form(forms.ModelForm):
    class Meta:
        model = Commentshop
        fields = ['body']