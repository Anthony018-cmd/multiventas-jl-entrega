# Entidad: Cliente. Es la persona que compra desde la web.


class Cliente:
    def __init__(self, id, nombre, correo, telefono=""):
        # Identidad obligatoria
        if id is None:
            raise ValueError("El cliente necesita un id")
        # Nombre obligatorio
        if not nombre or not nombre.strip():
            raise ValueError("El cliente necesita un nombre")
        # Validación simple del correo: debe contener una arroba
        if not correo or "@" not in correo:
            raise ValueError("El cliente necesita un correo válido")
        self.id = id  # identidad del cliente
        self.nombre = nombre.strip()  # nombre completo
        self.correo = correo  # correo de contacto
        self.telefono = telefono  # teléfono (opcional)
