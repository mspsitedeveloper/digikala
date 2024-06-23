from django.contrib import admin
from .models import Post , comment , tag

admin.site.register(Post)
admin.site.register(comment)
admin.site.register(tag)