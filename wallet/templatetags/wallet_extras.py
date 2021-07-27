from django import template
from wallet.models import *
from random import sample
import random
from django.db.models import Q
from django.template.defaultfilters import slugify


register = template.Library()

@register.simple_tag
def get_transacciones(profile):
    transacciones = Transaction.objects.filter(owner = profile)
    return transacciones

