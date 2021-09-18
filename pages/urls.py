from django.urls import path
from . import views
from .views import PageDetailView

urlpatterns = [
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
]
