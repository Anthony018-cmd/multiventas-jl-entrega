# Entidad: Producto. Es la raíz de su agregado.
from .dinero import Dinero


class Producto:
    def __init__(self, id, nombre, precio, categoria_id=None, imagen="", stock=0):
        # Identidad obligatoria
        if id is None:
            raise ValueError("El producto necesita un id")
        # Nombre obligatorio
        if not nombre or not nombre.strip():
            raise ValueError("El producto necesita un nombre")
        # El precio debe ser un Dinero (value object), no un número suelto
        if not isinstance(precio, Dinero):
            raise ValueError("El precio debe ser un objeto Dinero")
        # El stock es un entero mayor o igual a 0
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un entero mayor o igual a 0")
        self.id = id  # identidad del producto
        self.nombre = nombre.strip()  # nombre visible en el catálogo
        self.precio = precio  # precio como Dinero
        self.categoria_id = categoria_id  # referencia a la Categoria por id
        self.imagen = imagen  # URL de la imagen
        self.stock = stock  # unidades disponibles

    def hay_stock_para(self, cantidad: int) -> bool:
        # Regla de dominio: hay unidades suficientes para la cantidad pedida
        return self.stock >= cantidad
