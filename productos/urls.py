from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('category/<int:id>/<slug:slug>', CategoryListView.as_view(), name='category_list'),
    path('item/<int:id>/<slug:slug>', ItemDetailView.as_view(), name = 'item_detail'),
    path('ofertas/', OfferListView.as_view(), name = 'ofertas'),
]
