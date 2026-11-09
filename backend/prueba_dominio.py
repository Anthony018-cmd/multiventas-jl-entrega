# Prueba rápida del modelo de dominio.
# Ejecutar desde la carpeta backend:  python prueba_dominio.py
from domain import Dinero, Producto, Carrito, Pedido, ENVIO_SHALOM

# Creamos un producto con precio de 25.50 soles y 10 unidades de stock
funda = Producto(id=1, nombre="Funda para celular", precio=Dinero(25.5), categoria_id=1, stock=10)

# Creamos un carrito y agregamos 2 fundas
carrito = Carrito(id=1, cliente_id=1)
carrito.agregar_producto(funda, 2)
print("Total carrito:", carrito.total().formatear())

# Convertimos el carrito en pedido con envío por Shalom
pedido = Pedido.crear_desde_carrito(1, carrito, ENVIO_SHALOM)
print("Estado inicial:", pedido.estado)
pedido.marcar_pagado()
print("Estado después de pagar:", pedido.estado)
print("Total pedido:", pedido.total().formatear())

# Regla de dominio: pedir más que el stock lanza un error
try:
    carrito.agregar_producto(funda, 20)
except ValueError as e:
    print("Error esperado:", e)
