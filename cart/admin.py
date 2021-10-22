from django.contrib import admin
from .models import OrderItem, Order, Coupon, OrderStatus, Wish
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order

class CouponResource(resources.ModelResource):
    class Meta:
        model = Coupon

class OrderStatusResource(resources.ModelResource):
    class Meta:
        model = OrderStatus

class OrderItemResource(resources.ModelResource):
    class Meta:
        model = OrderItem

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('owner', 'ref_code', 'date_ordered',)
    list_display = ( 'id', 'owner', 'ref_code', 'is_ordered','date_ordered', 'total',)
    resourse_class = OrderResource

class OrderItemAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resourse_class = OrderItemResource

class OrderStatusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('id', 'name', 'date_created',)
    list_display = ( 'id', 'get_order', 'name', 'date_created',)

class CouponAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('id', 'code', 'amount', 'percentage', 'status')
    list_display = ( 'id', 'code', 'amount', 'percentage', 'status')



admin.site.register(Coupon, CouponAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)