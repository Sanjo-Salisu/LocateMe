from django.urls import path
from .views import index, location_view

urlpatterns = [
    path('', index),              # frontend
    path('api/location/', location_view),  # backend API
]