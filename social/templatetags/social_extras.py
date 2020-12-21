from django import template
from social.models import Email, Number

register = template.Library()

@register.simple_tag
def get_link_wha(numero, mensaje):
    numero_modif = "{}{}{}{}{}{}{}{}{}".format(
        numero[2],numero[3],numero[4],numero[6],numero[7],numero[8],numero[9],numero[10],numero[11]
        )
    cadena = "https://api.whatsapp.com/send?phone=595{}&text={}".format(numero_modif, mensaje)
    return cadena

@register.simple_tag
def get_link_wha_order(numero, order_number, link):
    numero_modif = "{}{}{}{}{}{}{}{}{}".format(
        numero[2],numero[3],numero[4],numero[6],numero[7],numero[8],numero[9],numero[10],numero[11]
        )
    texto= "Tengo un pedido en espera, Pedido Nº: {}".format(order_number)
    cadena = "https://api.whatsapp.com/send?phone=595{}&text={} {}".format(numero_modif, texto, link)
    return cadena

@register.simple_tag
def get_emails():
    emails = Email.objects.filter(estado = True)
    return emails

@register.simple_tag
def get_numbers():
    numbers = Number.objects.filter(estado = True)
    return numbers

@register.simple_tag
def get_number_one():
    number = Number.objects.get(id=1)
    value = number.number
    return number.number
