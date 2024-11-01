from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView , DetailView ,View
from .models import UserModel


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class Profile_page(DetailView):
    model = UserModel
    template_name = 'profile.html'