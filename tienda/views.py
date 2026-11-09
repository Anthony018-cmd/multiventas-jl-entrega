from django.shortcuts import render
from django.http import JsonResponse
from .repositories import ProductoRepository
from .factories import ProductoResponseFactory

def lista_productos(request):
    # Uso del patron Repository para consultar los datos
    repo = ProductoRepository()
    productos = repo.obtener_todos()
    
    # Uso del patron Factory para transformar los objetos a formato de respuesta
    data = [ProductoResponseFactory.crear_respuesta(prod) for prod in productos]
    
    return JsonResponse(data, safe=False)
# Create your views here.
