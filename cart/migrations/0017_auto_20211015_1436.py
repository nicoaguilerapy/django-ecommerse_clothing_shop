# Generated by Django 2.2.10 on 2021-10-15 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_auto_20211015_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 18, 14, 36, 3, 467917), verbose_name='Fecha de Entrega'),
        ),
    ]
