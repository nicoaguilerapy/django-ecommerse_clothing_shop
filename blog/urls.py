from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('<int:id>/<slug:slug>', PostDetailView.as_view(), name='detalles_post'),
]

