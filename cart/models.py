from django.db import models
from accounts.models import Profile
from productos.models import Item
from django_countries.fields import CountryField
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save, post_init
from social.models import Fact, Email
from accounts.models import CustomUser, Profile
from datetime import datetime
from datetime import timedelta

STATUS_CHOICES = (
    ('PE', 'Pendiente'),
    ('RE', 'Recibido'),
    ('EM', 'Empaquetado'),
    ('EC', 'En Camino'),
    ('LR', 'Listo Para Retiro'),
    ('PL', 'Problemas Logísticos'),
    ('CA', 'Cancelado'),
    ('RE', 'Retirado'),
)

class Coupon(models.Model):
    id = models.AutoField(primary_key = True)
    code = models.CharField('Código', max_length=15)
    amount = models.IntegerField('Descuento Fijo', default = 0)
    percentage = models.IntegerField('Porcentaje',  default = 0)
    status = models.BooleanField('Activo/Inactivo', default = True)
    
    class Meta:
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'

    def __str__(self):
        return self.code

class OrderItem(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    model = models.CharField('Modelo', max_length=255, null = False, blank = False, default = 'Vacio')
    size = models.CharField('Talle', max_length=255, null = False, blank = False, default = 'Vacio')
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(default = 1)
    
    class Meta:
        verbose_name = 'Articulo Pedido'
        verbose_name_plural = 'Articulos Pedidos'
    
    
    def get_item_total(self):
        if self.item.offer:
            value = self.item.price_offer*self.quantity
        else:
            value = self.item.price*self.quantity

        return value
    
    def __str__(self):
        return '{} - {} - {}'.format(self.owner, self.item, self.quantity)

class OrderStatus(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Estado', choices=STATUS_CHOICES, max_length=2, default='PE')
    date_created = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Estado del Pedido'
        verbose_name_plural = 'Estado de los Pedidos'

    def __str__(self):
        return '{} | {}'.format(self.name, self.date_created)

    def get_order(self):
        order_status = Order.objects.filter(status__in = [self])
        return order_status.first()
    get_order.short_description = 'Pedido'

class Order(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    ref_code = models.IntegerField(default = 1000)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    total = models.IntegerField('Total a Pagar', default = 0)
    date_delivery = models.DateTimeField('Fecha de Entrega', default = datetime.now() + timedelta(hours = 72))
    delivery_by = models.CharField('Enviado por', default="", max_length=255)
    tracking = models.CharField('Tracking', default="", max_length=255)
    status = models.ManyToManyField(OrderStatus)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        sum = 0
        for item in self.items.all():
            if item.item.offer:
                sum = (item.item.price_offer*item.quantity)+ sum
            else:
                sum = (item.item.price*item.quantity) + sum
            
        return sum
    
    def get_count(self):
        sum = 0
        for item in self.items.all():
            sum = sum + 1
        return sum

    def get_status(self):
        status = self.status.all()
        print("{} | get_status: {}".format(self, status))
        return status.last()

    def get_status_current(self):
        text = self.get_status().name
        if text == 'PE':
            return 'Pendiente'
        elif text == 'RE':
            return 'Recibido'
        elif text == 'EM':
            return 'Empaquetado'
        elif text == 'EC':
            return 'En Camino'
        elif text == 'LR':
            return 'Listo Para Retiro'
        elif text == 'PL':
            return 'Problemas Logísticos'
        elif text == 'CA':
            return 'Cancelado'
        elif text == 'RE':
            return 'Retirado'

          
    def __str__(self):
        return '{} - {} | {}'.format(self.id, self.owner, self.total)

class Wish(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    date_created = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)
    
    class Meta:
        verbose_name = 'Deseo'
        verbose_name_plural = 'Lista de Deseos'


# method for updating
@receiver(post_save, sender=Order, dispatch_uid="update_status_count")
def update_order(sender, instance, **kwargs):
    aux=0
    for stat in instance.status.all():
        if stat.name == 'PE':
            aux=1
    
    if aux == 0:
        order_status = OrderStatus.objects.create(name = 'PE')
        print("Estado creado")
        instance.status.add(order_status)

# method for updating
@receiver(post_save, sender=OrderStatus, dispatch_uid="update_status_count")
def update_orderstatus(sender, instance, **kwargs):
    print("Correo con el cambio")
    pass