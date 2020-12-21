from django.contrib import admin
from .models import OrderItem, Order, Coupon

class OrderAdmin(admin.ModelAdmin):
    model = Order
    search_fields = ('owner', 'ref_code', 'date_ordered','status',)
    list_display = ( 'id', 'owner', 'ref_code', 'is_ordered','date_ordered', 'status', 'total',)



admin.site.register(Coupon)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)