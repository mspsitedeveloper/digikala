from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from .views import success , home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'), name='blog'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls'), name='shop'),
    path('success/', success.as_view() , name='success'),
    path('', home.as_view() , name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)