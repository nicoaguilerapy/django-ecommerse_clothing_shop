from django.urls import path
from . import views
from .views import add_to_cart, my_cart, delete_from_cart, finish_order, OrderListView, order_detail, OrderAdminList, OrderAdminUpdate

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('', my_cart, name='my_cart'),
    path('delete-from-cart/', delete_from_cart, name='delete_from_cart'),
    path('finish-order/', finish_order, name='finish_order'),
    path('my-orders/', OrderListView.as_view(), name='order_list'),
    path('my-orders/<int:id>/', order_detail, name = 'detail_order'),
    path('my-orders/<int:id>/', order_detail, name = 'detail_order'),
    path('admin/order/', OrderAdminList.as_view(), name = 'admin_order_list'),
    path('admin/order/update/<int:pk>/', OrderAdminUpdate.as_view(), name = 'admin_order_edit'),
]