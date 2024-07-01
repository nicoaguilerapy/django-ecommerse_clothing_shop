from django import template
from productos.models import Item, Category, CoverPage
from random import sample
import random
from django.db.models import Q
from django.template.defaultfilters import slugify


register = template.Library()

@register.simple_tag
def get_modelos(id):
    modelos = Item.objects.get(id = id)
    return modelos.modelos.split(',')

@register.simple_tag
def get_talles(id):
    talles = Item.objects.get(id = id)
    return talles.talles.split(',')

@register.simple_tag
def multipli(a, b):
    c=(a*b)+1
    return c

@register.simple_tag
def get_cover_pages():
    portadas = CoverPage.objects.filter(visibility = True)
    return portadas

@register.simple_tag
def get_items(limit):
    items = Item.objects.filter(visibility = True)[:limit]
    return items

@register.simple_tag
def get_url_aleatoria(obj):
    items_list = Item.objects.filter(visibility = True, categories=obj.id)
    cantidad = items_list.count()
    print(cantidad)
    producto_random = random.sample(list(items_list), 1)
    print(producto_random)
    return producto_random

@register.simple_tag
def get_slug_categoria(id):
    categoria = Category.objects.get(id=int(id))
    return  slugify(categoria.nombre)

@register.simple_tag
def get_items_categoria(obj):
    cantidad_obj = obj.categories.all()
    items_all = Item.objects.filter(~Q(id = obj.id))
    items_list = items_all.filter(visibility = True, categories__in=cantidad_obj)
    cantidad = items_list.count()
    numeros = 4
    if cantidad < 4:
        items_list = items_all.filter(visibility = True)
    else:
        items_list = random.sample(list(items_list), numeros)
        
    
    return items_list


