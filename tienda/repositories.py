from .models import Producto

class ProductoRepository:
    # Método para obtener todos los productos de la tienda
    def obtener_todos(self):
        return Producto.objects.all()

    # Método para buscar un producto por su ID único
    def obtener_por_id(self, producto_id):
        try:
            return Producto.objects.get(pk=producto_id)
        except Producto.DoesNotExist:
            return None

    # Método para crear y guardar un nuevo producto en la base de datos
    def crear(self, datos):
        return Producto.objects.create(
            nombre=datos.get('nombre'),
            descripcion=datos.get('descripcion'),
            precio=datos.get('precio'),
            stock=datos.get('stock')
        )