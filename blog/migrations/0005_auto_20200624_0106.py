# Generated by Django 2.2.10 on 2020-06-24 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200624_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
