from django.urls import path
from .views import SignUp , Profile_page
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile<pk>/profile', Profile_page.as_view(), name='pro-profile'),
]