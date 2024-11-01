# Generated by Django 5.0.6 on 2024-10-03 09:50

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظر ها'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'هشتگ', 'verbose_name_plural': 'هشتگ ها'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='مقاله مادر'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2024, 10, 3), verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.TextField(verbose_name='عنوان'),
        ),
    ]