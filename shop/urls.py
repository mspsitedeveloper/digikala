from django.urls import path
from .views import (
    Home ,
    Single,
    UpdatePost,
    DeletePost,
    NewProduct,
)

urlpatterns = [
    path('', Home.as_view() , name='shop'),
    path('<slug>/', Single.as_view() , name='single-shop'),
    path('new', NewProduct.as_view() , name='new-product'),
    path('<slug>/update', UpdatePost.as_view() , name='update_product'),
    path('<slug>/delete', DeletePost.as_view() , name='delete_product'),
]