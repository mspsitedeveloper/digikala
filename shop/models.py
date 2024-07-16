from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name="عنوان")
    slug = models.SlugField(max_length=200,verbose_name="ادرس")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name="عنوان")
    desc = models.TextField(verbose_name="توضیحات")
    extract = models.TextField(verbose_name="خلاصه")
    slug = models.SlugField(verbose_name="ادرس")
    photo = models.ImageField(verbose_name="تصویر", upload_to="photo/%y/%m/%d")
    date = models.DateField(verbose_name="تاریخ", default=date.today())
    Price = models.IntegerField(verbose_name="قیمت")
    category = models.ForeignKey(to=Category , on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, verbose_name='نویسنده')

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصول ها"

    def __str__(self):
        return self.name
    
class Commentshop(models.Model):
    body = models.TextField(null=False, blank=False , verbose_name='متن')
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, verbose_name='نویسنده')
    date = models.DateField(default=date.today() , verbose_name='تاریخ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE , verbose_name='مقاله مادر')
    
    def __str__(self):
        return self.body
    
    class Meta():
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'