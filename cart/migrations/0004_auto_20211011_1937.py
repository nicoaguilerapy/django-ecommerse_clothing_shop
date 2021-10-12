# Generated by Django 2.2.10 on 2021-10-11 22:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20211006_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 14, 19, 37, 12, 21933), verbose_name='Fecha de Entrega'),
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PE', 'Pendiente'), ('RE', 'Recibido'), ('EN', 'En Camino'), ('LR', 'Listo Para Retirno'), ('PL', 'Problemas Logísticos')], default='PE', max_length=2, verbose_name='Estado')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.Order')),
            ],
        ),
    ]
