# Rutas de la app catalogo (endpoints principales del backend)
from django.urls import path

from . import views

urlpatterns = [
    path("productos/", views.productos),  # GET  /api/productos/
    path("pedidos/", views.crear_pedido),  # POST /api/pedidos/
]
