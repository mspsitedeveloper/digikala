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

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصول ها"

    def __str__(self):
        return self.name