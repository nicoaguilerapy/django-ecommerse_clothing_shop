from django import template
from pages.models import Page, Destacado

register = template.Library()

@register.simple_tag
def get_pages():
    pages = Page.objects.filter(estado = True)
    return pages

@register.simple_tag
def get_destacados():
    destacados = Destacado.objects.filter(estado = True)
    return destacados

@register.simple_tag
def get_page_sn():
    page = Page.objects.get(id=1)
    return page
    
