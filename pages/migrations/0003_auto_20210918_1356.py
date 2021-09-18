# Generated by Django 2.2.10 on 2021-09-18 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_delete_destacado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title'], 'verbose_name': 'Pagina', 'verbose_name_plural': 'Paginas'},
        ),
        migrations.RenameField(
            model_name='page',
            old_name='contenido',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='fecha_creacion',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='fecha_modificacion',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='orden',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='estado',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='nombre',
            new_name='title',
        ),
    ]