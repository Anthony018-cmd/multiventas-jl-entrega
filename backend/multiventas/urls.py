# Rutas principales: todo lo que empiece con /api/ lo atiende la app catalogo
from django.urls import include, path

urlpatterns = [
    path("api/", include("catalogo.urls")),
]
