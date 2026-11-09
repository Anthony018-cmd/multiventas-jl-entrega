class ProductoResponseFactory:
    """Factory que transforma una entidad de dominio en respuesta JSON."""
    @staticmethod
    def crear(producto, nombres_categorias):
        return {'id': producto.id, 'nombre': producto.nombre, 'precio': float(producto.precio.monto), 'categoria': nombres_categorias.get(producto.categoria_id, ''), 'imagen': producto.imagen, 'stock': producto.stock}
