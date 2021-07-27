from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('my-wallet/', MyWalletView.as_view(), name='my_wallet'),
    path('order/', OrderView.as_view(), name='wallet_order'),
    path('history/', HistoryView.as_view(), name='wallet_history'),
]