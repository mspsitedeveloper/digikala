from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    photo = models.ImageField(
        upload_to='photo/profile/%Y/%m/%d/' , verbose_name='عکس پروفایل')
    about = models.CharField(max_length=255 , verbose_name='معرفی')