# Generated by Django 2.2.10 on 2020-06-22 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20200621_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(default='titulo'),
        ),
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(default='titulo'),
        ),
    ]
