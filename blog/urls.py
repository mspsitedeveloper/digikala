from django.urls import path
from .views import (
    Home ,
    NewPost ,
    Single ,
    DeletePost ,
    UpdatePost,
    Search ,
)
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/new', NewPost.as_view(), name='new_post'),
    path('post/<int:pk>', Single.as_view(), name="single"),
    path('post/update/<int:pk>' , UpdatePost.as_view() , name='update_post'),
    path('post/delete/<int:pk>' , DeletePost.as_view() , name='delete_post'),
    path('search' , Search.as_view() , name='search'),
]