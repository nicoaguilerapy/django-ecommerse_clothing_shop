# Generated by Django 2.2.10 on 2021-09-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210918_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Casa Fenix', max_length=90, verbose_name='Titulo'),
        ),
    ]
