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
    path('', Home.as_view(), name='blog'),
    path('post/new', NewPost.as_view(), name='new_post'),
    path('post/<int:pk>', Single.as_view(), name="single-post"),
    path('post/update/<int:pk>' , UpdatePost.as_view() , name='update_post'),
    path('post/delete/<int:pk>' , DeletePost.as_view() , name='delete_post'),
    path('search/' , Search.as_view() , name='search'),
]