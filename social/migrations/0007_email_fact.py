# Generated by Django 2.2 on 2020-06-30 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20200630_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='fact',
            field=models.CharField(default=1, max_length=100, verbose_name='Categoria del Email'),
            preserve_default=False,
        ),
    ]