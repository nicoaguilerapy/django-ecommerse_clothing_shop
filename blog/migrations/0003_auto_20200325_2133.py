# Generated by Django 3.0.4 on 2020-03-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200324_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(related_name='get_posts', to='blog.Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(upload_to='blog'),
        ),
    ]
