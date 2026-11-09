# Value Object: LineaPedido. Copia de un item del carrito al confirmar la compra.
from dataclasses import dataclass
from .dinero import Dinero


@dataclass(frozen=True)  # frozen = inmutable: el historial de compra no debe cambiar
class LineaPedido:
    producto_id: int  # id del producto comprado
    nombre: str  # nombre en el momento de la compra
    precio_unitario: Dinero  # precio congelado al comprar
    cantidad: int  # unidades compradas

    def __post_init__(self):
        # La cantidad debe ser un entero de al menos 1
        if not isinstance(self.cantidad, int) or self.cantidad < 1:
            raise ValueError("La cantidad debe ser un entero mayor o igual a 1")
        # El precio unitario debe ser un Dinero
        if not isinstance(self.precio_unitario, Dinero):
            raise ValueError("El precio unitario debe ser un objeto Dinero")

    @staticmethod
    def desde_item(item) -> "LineaPedido":
        # Crea una LineaPedido a partir de un ItemCarrito
        return LineaPedido(
            item.producto_id, item.nombre, item.precio_unitario, item.cantidad
        )

    def subtotal(self) -> Dinero:
        # Subtotal de la línea = precio unitario x cantidad
        return self.precio_unitario.multiplicar(self.cantidad)
