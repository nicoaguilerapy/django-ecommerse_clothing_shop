from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('', my_cart, name='my_cart'),
    path('ajax/my-cart/', MyCartList.as_view(), name='my_cart_ajax'),
    path('delete-from-cart/', delete_from_cart, name='delete_from_cart'),
    path('finish-order/', finish_order, name='finish_order'),
    path('my-orders/', OrderListView.as_view(), name='order_list'),
    path('wishlist/', WishListView.as_view(), name='my_wish'),
    path('add-to-wishlist/', add_wishlist, name='add_to_wishlist'),
    path('delete-from-wish/', delete_from_wish, name='delete_from_wish'),
    path('my-orders/<int:id>/', order_detail, name = 'order_detail'),
    path('admin/order/', OrderAdminList.as_view(), name = 'admin_order_list'),
    path('admin/order/update/<int:pk>/', OrderAdminUpdate.as_view(), name = 'admin_order_edit'),

    path('delete_all_orderstatus/', delete_all_orderstatus, name='delete_all_orderstatus'),
    path('delete_all_order/', delete_all_order, name='delete_all_order'),
]