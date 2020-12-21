# Generated by Django 2.2 on 2020-06-30 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_destacado_pagina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='subtitulo',
        ),
        migrations.AlterField(
            model_name='page',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Visible/Invisible'),
        ),
        migrations.AlterField(
            model_name='page',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Titulo de la Pagina'),
        ),
    ]
