# Entidad: Categoria. Agrupa productos (por ejemplo "Fundas" o "Cargadores").


class Categoria:
    def __init__(self, id, nombre):
        # Una entidad siempre tiene identidad: el id
        if id is None:
            raise ValueError("La categoría necesita un id")
        # El nombre es obligatorio y no puede estar vacío
        if not nombre or not nombre.strip():
            raise ValueError("La categoría necesita un nombre")
        self.id = id  # identidad de la categoría
        self.nombre = nombre.strip()  # nombre sin espacios sobrantes
