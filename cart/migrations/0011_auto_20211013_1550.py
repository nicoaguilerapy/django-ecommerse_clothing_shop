# Generated by Django 2.2.10 on 2021-10-13 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_auto_20211013_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='estado',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 16, 15, 50, 49, 269024), verbose_name='Fecha de Entrega'),
        ),
    ]
