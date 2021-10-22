from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('', ItemListView.as_view(), name='product_list'),
    path('categoria/<int:id>/<slug:slug>', CategoryListView.as_view(), name='categoria'),
    path('producto/<int:id>/<slug:slug>', ItemDetailView.as_view(), name = 'product_detail'),
    path('ofertas/', OfferListView.as_view(), name = 'ofertas'),
]
