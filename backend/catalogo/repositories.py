from .datos import PRODUCTOS, buscar_producto


class ProductoRepository:
    """Repository que centraliza la lectura del catálogo del prototipo."""
    def obtener_todos(self):
        return list(PRODUCTOS)
    def obtener_por_id(self, producto_id):
        return buscar_producto(producto_id)
