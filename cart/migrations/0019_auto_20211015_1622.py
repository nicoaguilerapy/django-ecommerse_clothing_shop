# Generated by Django 2.2.10 on 2021-10-15 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0018_auto_20211015_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 18, 16, 22, 31, 932155), verbose_name='Fecha de Entrega'),
        ),
    ]