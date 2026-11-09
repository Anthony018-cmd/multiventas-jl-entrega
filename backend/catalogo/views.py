import itertools
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from domain import Carrito, Pedido
from .datos import CATEGORIAS
from .factories import ProductoResponseFactory
from .repositories import ProductoRepository

_ids_pedido = itertools.count(1)
productos_repo = ProductoRepository()

def productos(request):
    nombres = {c.id: c.nombre for c in CATEGORIAS}
    datos = [ProductoResponseFactory.crear(p, nombres) for p in productos_repo.obtener_todos()]
    return JsonResponse(datos, safe=False)

@csrf_exempt
def crear_pedido(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Usa el método POST'}, status=405)
    try:
        cuerpo = json.loads(request.body)
        carrito = Carrito(id=1, cliente_id=cuerpo.get('cliente_id', 1))
        for item in cuerpo.get('items', []):
            producto = productos_repo.obtener_por_id(item['producto_id'])
            if producto is None:
                raise ValueError('Producto no existe')
            carrito.agregar_producto(producto, item['cantidad'])
        pedido = Pedido.crear_desde_carrito(next(_ids_pedido), carrito, cuerpo.get('metodo_entrega'))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        return JsonResponse({'error': str(error)}, status=400)
    return JsonResponse({'id': pedido.id, 'estado': pedido.estado, 'metodo_entrega': pedido.metodo_entrega, 'lineas': [{'nombre': l.nombre, 'cantidad': l.cantidad, 'subtotal': float(l.subtotal().monto)} for l in pedido.lineas], 'total': float(pedido.total().monto)}, status=201)
