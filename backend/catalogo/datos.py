# Datos de ejemplo del catálogo de MULTIVENTAS JL (accesorios y equipos celulares).
from domain import Categoria, Dinero, Producto

# Categorías del catálogo
CATEGORIAS = [
    Categoria(1, "Fundas"),
    Categoria(2, "Cargadores"),
    Categoria(3, "Audífonos"),
    Categoria(4, "Celulares"),
]

# Productos del catálogo (precio en soles)
PRODUCTOS = [
    Producto(1, "Funda transparente", Dinero(15), 1, "", 25),
    Producto(2, "Funda antigolpes", Dinero(25), 1, "", 15),
    Producto(3, "Cargador rápido 20W", Dinero(35), 2, "", 12),
    Producto(4, "Cable USB-C 1m", Dinero(12), 2, "", 40),
    Producto(5, "Audífonos Bluetooth", Dinero(79.9), 3, "", 8),
    Producto(6, "Celular 128GB", Dinero(799), 4, "", 3),
]


def buscar_producto(producto_id):
    # Devuelve el Producto con ese id, o None si no existe
    return next((p for p in PRODUCTOS if p.id == producto_id), None)
