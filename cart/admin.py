from django.contrib import admin
from .models import OrderItem, Order, Coupon, Wish
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order

class OrderItemResource(resources.ModelResource):
    class Meta:
        model = OrderItem

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('owner', 'ref_code', 'date_ordered','status',)
    list_display = ( 'id', 'owner', 'ref_code', 'is_ordered','date_ordered', 'status', 'total',)
    resourse_class = OrderResource

class OrderItemAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resourse_class = OrderItemResource



admin.site.register(Coupon)
admin.site.register(Wish)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)