from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('my-wallet/', MyWalletView.as_view(), name='my_wallet'),
]