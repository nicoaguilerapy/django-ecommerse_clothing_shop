# Generated by Django 2.2 on 2020-07-01 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_auto_20200630_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='category',
            field=models.CharField(default=1, max_length=100, verbose_name='Categoria del Número'),
            preserve_default=False,
        ),
    ]
