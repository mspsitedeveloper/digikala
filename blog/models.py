from django.db import models
from datetime import date
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50 , verbose_name='عنوان')
    abstract = models.TextField(verbose_name='خلاصه')
    body = models.TextField(verbose_name='محتوا')
    author = models.ForeignKey('accounts.UserModel', on_delete=models.CASCADE, verbose_name='نویسنده')
    date = models.DateField(default=date.today(), verbose_name='تاریخ')
    photo = models.ImageField(upload_to='photo/%y/%m/%d', verbose_name='تصویر')
    tag = models.ForeignKey('blog.tag', on_delete=models.CASCADE, verbose_name='هشتگ')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("single", kwargs={'pk': self.pk })
    
    class Meta():
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
    
class comment(models.Model):
    body = models.TextField(null=False, blank=False , verbose_name='متن')
    author = models.ForeignKey('accounts.UserModel', on_delete=models.CASCADE, verbose_name='نویسنده')
    date = models.DateField(default=timezone.now , verbose_name='تاریخ')
    post = models.ForeignKey(Post, on_delete=models.CASCADE , verbose_name='مقاله مادر')
    
    def __str__(self):
        return self.body
    
    class Meta():
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'
    
class tag(models.Model):
    title = models.TextField(null=False, blank=False , verbose_name='عنوان')
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = 'هشتگ'
        verbose_name_plural = 'هشتگ ها'