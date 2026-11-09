# Configuración mínima de Django para el prototipo de MULTIVENTAS JL.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # carpeta raíz del backend

SECRET_KEY = "clave-solo-para-prototipo"  # en producción iría en una variable de entorno
DEBUG = True  # modo desarrollo
ALLOWED_HOSTS = ["*"]  # el prototipo corre solo en local

INSTALLED_APPS = ["catalogo"]  # nuestra app con los endpoints

MIDDLEWARE = [
    "catalogo.middleware.CorsMiddleware",  # permite que el front (otro puerto) llame a la API
]

ROOT_URLCONF = "multiventas.urls"  # archivo con las rutas principales
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True

# Prototipo: los datos viven en memoria (catalogo/datos.py).
# En el sistema real, la base de datos sería PostgreSQL (justificado en el informe).
DATABASES = {}
