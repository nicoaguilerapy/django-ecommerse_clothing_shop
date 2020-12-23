# Generated by Django 2.2.10 on 2020-06-23 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_auto_20200622_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='slug',
        ),
        migrations.CreateModel(
            name='Portada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo del Producto')),
                ('subtitulo', models.CharField(max_length=100, verbose_name='Titulo del Producto')),
                ('orden', models.IntegerField(default=5, verbose_name='Orden de Prioridades')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('id_categoria', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='productos.Categoria')),
            ],
            options={
                'verbose_name': 'Portada',
                'verbose_name_plural': 'Portadas',
                'ordering': ['orden', 'fecha_creacion'],
            },
        ),
    ]