from django import template
from productos.models import Producto, Categoria, Portada
from random import sample
import random
from django.db.models import Q
from django.template.defaultfilters import slugify


register = template.Library()

@register.simple_tag
def get_modelos(id):
    modelos = Producto.objects.get(id = id)
    return modelos.modelos.split(',')

@register.simple_tag
def get_talles(id):
    talles = Producto.objects.get(id = id)
    return talles.talles.split(',')

@register.simple_tag
def multipli(a, b):
    c=(a*b)+1
    return c

@register.simple_tag
def get_portadas():
    portadas = Portada.objects.filter(estado = True)
    return portadas

@register.simple_tag
def get_productos(limit):
    productos = Producto.objects.filter(estado = True)[:limit]
    return productos

@register.simple_tag
def get_url_aleatoria(obj):
    productos_list = Producto.objects.filter(estado = True, categorias=obj.id)
    cantidad = productos_list.count()
    print(cantidad)
    producto_random = random.sample(list(productos_list), 1)
    print(producto_random)
    return producto_random

@register.simple_tag
def get_slug_categoria(id):
    categoria = Categoria.objects.get(id=int(id))
    return  slugify(categoria.nombre)

@register.simple_tag
def get_productos_categoria(obj):
    cantidad_obj = obj.categorias.all()
    productos_all = Producto.objects.filter(~Q(id = obj.id))
    productos_list = productos_all.filter(estado = True, categorias__in=cantidad_obj)
    cantidad = productos_list.count()
    numeros = 4
    if cantidad < 4:
        productos_list = productos_all.filter(estado = True)
        
    productos_aleatorios = random.sample(list(productos_list), numeros)
    return productos_aleatorios


