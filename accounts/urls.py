from django.urls import path, include
from . import views
from .views import ProfileUpdate


urlpatterns = [
    path('profile/', ProfileUpdate.as_view(), name='my_profile'),
]