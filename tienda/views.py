from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# --- MODULO DE PRODUCTOS ---
def lista_productos(request):
    if request.method == 'GET':
        # Aqui puedes usar tu ProductoRepository y ProductoResponseFactory
        data = [
            {"id": 1, "nombre": "Producto 1", "precio_venta": 15.5, "stock_actual": 10, "estado": "Disponible"}
        ]
        return JsonResponse(data, safe=False)

# --- MODULO DE CARRITO ---
@csrf_exempt
def agregar_carrito(request):
    if request.method == 'POST':
        return JsonResponse({"mensaje": "Producto agregado al carrito con exito"}, status=201)
    return JsonResponse({"error": "Metodo no permitido"}, status=405)

# --- MODULO DE USUARIOS ---
@csrf_exempt
def login_usuario(request):
    if request.method == 'POST':
        return JsonResponse({"mensaje": "Inicio de sesion exitoso", "token": "abc123xyz"}, status=200)
    return JsonResponse({"error": "Metodo no permitido"}, status=405)