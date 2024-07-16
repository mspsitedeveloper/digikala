from django.views.generic import ListView
from blog.models import Post

class success(ListView):
    template_name = 'success-page.html'
    model = Post

class home(ListView):
    template_name = 'home.html'
    model = Post