# Generated by Django 2.2.10 on 2021-10-12 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20211011_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 14, 19, 20, 873429), verbose_name='Fecha de Entrega'),
        ),
    ]
