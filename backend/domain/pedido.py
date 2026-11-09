# Entidad: Pedido. Raíz del agregado: las líneas solo se leen desde aquí.
from datetime import datetime
from .dinero import Dinero
from .linea_pedido import LineaPedido

# Estados posibles de un pedido
PENDIENTE = "PENDIENTE"
PAGADO = "PAGADO"
ENTREGADO = "ENTREGADO"
CANCELADO = "CANCELADO"

# Formas de entrega que ofrece la tienda
RECOJO = "RECOJO"
ENVIO_SHALOM = "ENVIO_SHALOM"
METODOS_ENTREGA = (RECOJO, ENVIO_SHALOM)


class Pedido:
    def __init__(self, id, cliente_id, lineas, metodo_entrega, estado=PENDIENTE, fecha=None):
        # Identidad obligatoria
        if id is None:
            raise ValueError("El pedido necesita un id")
        # Regla: un pedido tiene al menos una línea
        if not lineas:
            raise ValueError("El pedido necesita al menos una línea")
        # El método de entrega debe ser uno de los permitidos
        if metodo_entrega not in METODOS_ENTREGA:
            raise ValueError("Método de entrega no válido")
        self.id = id  # identidad del pedido
        self.cliente_id = cliente_id  # cliente que compró
        self.lineas = list(lineas)  # líneas compradas
        self.metodo_entrega = metodo_entrega  # recojo o envío por Shalom
        self.estado = estado  # estado actual del pedido
        self.fecha = fecha or datetime.now()  # fecha de creación

    @staticmethod
    def crear_desde_carrito(id, carrito, metodo_entrega) -> "Pedido":
        # Regla: no se puede crear un pedido con el carrito vacío
        if carrito.esta_vacio():
            raise ValueError("No se puede crear un pedido con el carrito vacío")
        # Cada item del carrito se copia como una LineaPedido
        lineas = [LineaPedido.desde_item(item) for item in carrito.items]
        return Pedido(id, carrito.cliente_id, lineas, metodo_entrega)

    def total(self) -> Dinero:
        # Total del pedido: suma de los subtotales de las líneas
        total = Dinero(0)
        for linea in self.lineas:
            total = total.sumar(linea.subtotal())
        return total

    def marcar_pagado(self):
        # Solo un pedido PENDIENTE se puede pagar
        if self.estado != PENDIENTE:
            raise ValueError("Solo un pedido pendiente se puede pagar")
        self.estado = PAGADO

    def marcar_entregado(self):
        # Solo un pedido PAGADO se puede entregar
        if self.estado != PAGADO:
            raise ValueError("Solo un pedido pagado se puede entregar")
        self.estado = ENTREGADO

    def cancelar(self):
        # Un pedido ya entregado no se puede cancelar
        if self.estado == ENTREGADO:
            raise ValueError("Un pedido entregado no se puede cancelar")
        self.estado = CANCELADO
