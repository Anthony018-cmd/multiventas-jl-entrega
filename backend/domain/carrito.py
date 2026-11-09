# Entidad: Carrito. Raíz del agregado: los items solo se tocan desde aquí.
from .dinero import Dinero
from .item_carrito import ItemCarrito


class Carrito:
    def __init__(self, id, cliente_id):
        # Identidad obligatoria
        if id is None:
            raise ValueError("El carrito necesita un id")
        self.id = id  # identidad del carrito
        self.cliente_id = cliente_id  # dueño del carrito
        self._items = []  # lista interna (el guion bajo indica "no tocar desde afuera")

    @property
    def items(self):
        # Devuelve una copia para que no se pueda alterar desde afuera
        return list(self._items)

    def agregar_producto(self, producto, cantidad=1):
        # Regla: no se puede pedir más que el stock
        if not producto.hay_stock_para(cantidad):
            raise ValueError(f"Stock insuficiente para {producto.nombre}")
        # Buscamos si el producto ya está en el carrito
        existente = next((i for i in self._items if i.producto_id == producto.id), None)
        if existente:
            nueva_cantidad = existente.cantidad + cantidad
            # Volvemos a validar el stock con la cantidad total
            if not producto.hay_stock_para(nueva_cantidad):
                raise ValueError(f"Stock insuficiente para {producto.nombre}")
            # Reemplazamos el item viejo por uno nuevo con la cantidad actualizada
            self._items = [
                i.con_cantidad(nueva_cantidad) if i.producto_id == producto.id else i
                for i in self._items
            ]
        else:
            # Si no existía, creamos un item nuevo
            self._items.append(
                ItemCarrito(producto.id, producto.nombre, producto.precio, cantidad)
            )

    def quitar_producto(self, producto_id):
        # Quita un producto del carrito por su id
        self._items = [i for i in self._items if i.producto_id != producto_id]

    def esta_vacio(self) -> bool:
        # Indica si el carrito no tiene items
        return len(self._items) == 0

    def total(self) -> Dinero:
        # Total del carrito: suma de los subtotales de cada item
        total = Dinero(0)
        for item in self._items:
            total = total.sumar(item.subtotal())
        return total
