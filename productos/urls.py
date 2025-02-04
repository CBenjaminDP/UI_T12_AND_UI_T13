from django.urls import path
from .views import *

urlpatterns = [
    path('', indexProductos, name='indexProductos'),
    path('api/get/', Lista_productos, name='lista'),
    path('registro/', registro, name='registro'),
]