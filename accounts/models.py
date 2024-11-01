from django.db import models
from django.contrib.auth.models import AbstractUser , AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
class UserModel(AbstractUser):
    photo = models.ImageField(
        upload_to='photo/profile/%Y/%m/%d/' , verbose_name='عکس پروفایل')
    about = models.CharField(max_length=255 , verbose_name='معرفی')
    name = models.CharField(max_length=30,verbose_name="نام")
    family = models.CharField(max_length=30,verbose_name="نام خانوادگی")
    is_shopper = models.BooleanField(default=False)

# class UserModel(AbstractBaseUser):
#     username_validator = UnicodeUsernameValidator()
#     # username = models.CharField(max_length=10,verbose_name="نام کاربری",unique=True)
#     photo = models.ImageField(upload_to='photo/profile/%Y/%m/%d/' , verbose_name='عکس پروفایل')
#     name = models.CharField(max_length=30,verbose_name="نام")
#     family = models.CharField(max_length=30,verbose_name="نام خانوادگی")
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     email = models.EmailField(max_length=254,unique=True)
#     is_shopper = models.BooleanField(default=False)
#     username = models.CharField(
#         max_length=150,
#         unique=True,
#         help_text=(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         validators=[username_validator],
#         error_messages={
#             "unique": ("A user with that username already exists."),
#         },
#     )
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email","name","family"]

    