from accounts.models import Profile
from cart.models import Order, OrderItem, OrderStatus
from django import template

register = template.Library()

@register.simple_tag
def get_order(user_profile):
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    return user_order

@register.simple_tag
def get_status_exist(user_order, status_aux):
    print("get_status_exist: {}".format(status_aux))
    for stat in user_order.status.all():
        if stat.name == status_aux:
            print("True")
            return True

    print("False")
    return False

@register.simple_tag
def get_order_count(order):
    sum = 0
    for item in order.items.all():
        sum = sum + 1
        
    return sum

@register.simple_tag
def get_discount(order, percentage):
    value = order.get_cart_total()
    discount = (value*percentage)/100
    return discount

@register.simple_tag
def get_sum_total(a, b, c):
    r = a - b - c
    return r

@register.simple_tag
def get_order_total(order):
    try:
        value = int(order.get_cart_total())
        print("order total {}".format(value))
    except:
        value = 0
    return value

@register.simple_tag
def setvar(val):
  return val

