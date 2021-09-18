from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('v2/', Index2.as_view(), name='home2'),
]