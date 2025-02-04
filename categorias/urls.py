from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_categoria, name='registrar_categoria'),
    path('api/get/', views.get_categorias, name='get_categorias'),
    path('json/', views.mostrar_categorias, name='mostrar_categorias'),
]
