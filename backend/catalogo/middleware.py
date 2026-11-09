# Middleware CORS simple: el front (Astro, puerto 4321) y la API (Django, puerto 8000)
# están en puertos distintos; sin esto el navegador bloquearía las peticiones.
from django.http import HttpResponse


class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # siguiente paso en la cadena de Django

    def __call__(self, request):
        # El navegador manda primero una petición OPTIONS para preguntar si puede llamar
        if request.method == "OPTIONS":
            respuesta = HttpResponse(status=204)
        else:
            respuesta = self.get_response(request)
        # Permitimos cualquier origen (solo para el prototipo)
        respuesta["Access-Control-Allow-Origin"] = "*"
        respuesta["Access-Control-Allow-Headers"] = "Content-Type"
        respuesta["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        return respuesta
