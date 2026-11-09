# Value Object: ItemCarrito. Una línea del carrito (producto + cantidad).
from dataclasses import dataclass, replace
from .dinero import Dinero


@dataclass(frozen=True)  # frozen = inmutable
class ItemCarrito:
    producto_id: int  # id del producto referenciado
    nombre: str  # nombre guardado para mostrar
    precio_unitario: Dinero  # precio de una unidad
    cantidad: int  # unidades en el carrito

    def __post_init__(self):
        # La cantidad debe ser un entero de al menos 1
        if not isinstance(self.cantidad, int) or self.cantidad < 1:
            raise ValueError("La cantidad debe ser un entero mayor o igual a 1")
        # El precio unitario debe ser un Dinero
        if not isinstance(self.precio_unitario, Dinero):
            raise ValueError("El precio unitario debe ser un objeto Dinero")

    def subtotal(self) -> Dinero:
        # Subtotal de la línea = precio unitario x cantidad
        return self.precio_unitario.multiplicar(self.cantidad)

    def con_cantidad(self, nueva_cantidad: int) -> "ItemCarrito":
        # Devuelve un ItemCarrito nuevo con otra cantidad
        return replace(self, cantidad=nueva_cantidad)
