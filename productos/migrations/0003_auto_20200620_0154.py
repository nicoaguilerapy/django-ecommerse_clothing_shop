# Generated by Django 2.2.10 on 2020-06-20 05:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['-orden'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['-orden', 'id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='categoria',
            name='orden',
            field=models.IntegerField(default=5, verbose_name='Orden de Prioridades'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='orden',
            field=models.IntegerField(default=5, verbose_name='Orden de Prioridades'),
        ),
    ]
