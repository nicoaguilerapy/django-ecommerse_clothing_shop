from django.db import models
from accounts.models import Profile
from productos.models import Producto
from django_countries.fields import CountryField
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from social.models import Fact, Email
from accounts.models import CustomUser, Profile

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
        return '{} - {} | {}'.format(self.owner, self.id, self.total)

class Whish(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = 'Deseo'
        verbose_name_plural = 'Lista de Deseos'


# method for updating
@receiver(post_save, sender=Order, dispatch_uid="update_status_count")
def update_status(sender, instance, **kwargs):
    if instance.is_ordered == True:

        dato_url = Fact.objects.get(slug = "dato_url")
        correo_pag = Email.objects.get(id = 1)
        perfil = Profile.objects.get(user = instance.owner.id)
        correo_per = perfil.user.email
        fecha = instance.date_ordered.strftime("%d-%m-%Y %H:%M:%S")
        estado_full = instance.status

        link = "{}/cart/my-orders/{}/".format(dato_url.value, instance.id)


        if estado_full == 'FI':
            estado = 'Finalizado'
        elif estado_full == 'CA':
            estado = 'Cancelado'
        elif estado_full == 'PR':
            estado = 'En Proceso'
        else:
            estado = 'Pendiente'

        try:
            send_mail(
                    "Pedido Nº {}".format(instance.id),
                    "Tu Pedido actualmente está en estado: {}\nPedido creado el {}\nMira tu pedido: {}".format(estado, fecha, link),
                    correo_pag.email,
                    [correo_per, correo_pag.email],
                    fail_silently=False,
                    )
            print("Correo Enviado")
        except:
            print("Correo no Enviado")

    


