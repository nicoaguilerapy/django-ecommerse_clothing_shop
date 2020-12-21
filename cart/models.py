from django.db import models
from accounts.models import Profile
from productos.models import Producto
from django_countries.fields import CountryField

STATUS_CHOICES = (
    ('PE', 'Pendiente'),
    ('PR', 'Proceso'),
    ('FI', 'Finalizado'),
    ('CA', 'Cancelado')
)

class Coupon(models.Model):
    id = models.AutoField(primary_key = True)
    code = models.CharField('Código', max_length=15)
    amount = models.IntegerField('Descuento Fijo', default = 0)
    percentage = models.IntegerField('Porcentaje',  default = 0)
    estado = models.BooleanField('Activo/Inactivo', default = True)
    
    class Meta:
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'

    def __str__(self):
        return self.code

class OrderItem(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
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
        if self.producto.oferta:
            value = self.producto.precio_oferta*self.quantity
        else:
            value = self.producto.precio*self.quantity

        return value
    
    def __str__(self):
        return '{} - {} - {}'.format(self.owner, self.producto, self.quantity)
   
class Order(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    ref_code = models.IntegerField(default = 1000)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    status = models.CharField('Estado', choices=STATUS_CHOICES, max_length=2, default='PE')
    total = models.IntegerField('Total a Pagar', default = 0)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        sum = 0
        for item in self.items.all():
            if item.producto.oferta:
                sum = (item.producto.precio_oferta*item.quantity)+ sum
            else:
                sum = (item.producto.precio*item.quantity) + sum
            
        return sum
    
    def get_count(self):
        sum = 0
        for item in self.items.all():
            sum = sum + 1
        return sum

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.id)


