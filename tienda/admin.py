from django.contrib import admin
from .models import Categoria, Producto, Perfil, Carrito, ItemCarrito, Pedido, LineaPedido

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Perfil)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Pedido)
admin.site.register(LineaPedido)
