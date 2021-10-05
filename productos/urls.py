from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('', ProductosListView.as_view(), name='product_list'),
    path('categoria/<int:id>/<slug:slug>', CategoriaListView.as_view(), name='categoria'),
    path('producto/<int:id>/<slug:slug>', ProductoDetailView.as_view(), name = 'product_detail'),
    path('ofertas/', OfertasListView.as_view(), name = 'ofertas'),
    path('management/product_list/', ProductoAdminListView.as_view(), name='admin_product_list'),
    path('management/product_create/', ProductoAdminCreateView.as_view(), name='admin_product_create'),
    path('management/product_edit/<int:pk>/', ProductoAdminUpdateView.as_view(), name='admin_product_edit'),
    path('management/product_delete/<int:pk>/', ProductoAdminDelete.as_view(), name='admin_product_delete'),
]
