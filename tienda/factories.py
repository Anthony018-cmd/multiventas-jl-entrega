class ProductoResponseFactory:
    """Clase encargada de formatear la estructura JSON de la entidad Producto."""

    @staticmethod
    def crear_respuesta_producto(producto):
        # Determina el estado de disponibilidad segun la cantidad de stock
        estado = "Disponible" if producto.stock > 0 else "Agotado"

        # Retorna un diccionario estructurado listo para ser serializado a JSON
        return {
            "id": producto.id,                           # Identificador unico
            "title": producto.nombre,                     # Nombre comercial
            "description": producto.descripcion or "",    # Detalle del producto
            "price": float(producto.precio),             # Valor unitario convertido a decimal
            "stockCount": producto.stock,                # Cantidad disponible en tienda
            "status": estado                              # Estado dinamico de inventario
        }

    @staticmethod
    def crear_lista_productos(productos):
        # Itera sobre la lista de objetos y aplica la fabrica a cada uno
        return [ProductoResponseFactory.crear_respuesta_producto(p) for p in productos]