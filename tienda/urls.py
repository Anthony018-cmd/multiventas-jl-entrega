from django.urls import path
from .views import lista_productos, agregar_carrito, login_usuario

urlpatterns = [
    # Modulo de Productos
    path('productos/', lista_productos, name='lista_productos'),
    
    # Modulo de Carrito
    path('carrito/agregar/', agregar_carrito, name='agregar_carrito'),
    
    # Modulo de Usuarios
    path('usuarios/login/', login_usuario, name='login_usuario'),
]