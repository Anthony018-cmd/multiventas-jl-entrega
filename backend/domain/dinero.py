# Value Object: Dinero.
# Se compara por valor (monto + moneda) y es inmutable (frozen=True).
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True)
class Dinero:
    monto: Decimal  # cantidad de dinero
    moneda: str = "PEN"  # PEN = soles peruanos

    def __post_init__(self):
        # Convertimos a Decimal (más exacto que float) y redondeamos a 2 decimales
        monto = Decimal(str(self.monto)).quantize(Decimal("0.01"), ROUND_HALF_UP)
        # Regla de dominio: el monto no puede ser negativo
        if monto < 0:
            raise ValueError("El monto debe ser mayor o igual a 0")
        # Como la clase es inmutable, usamos object.__setattr__ solo aquí, al crearla
        object.__setattr__(self, "monto", monto)

    def sumar(self, otro: "Dinero") -> "Dinero":
        # Regla: solo se pueden sumar montos de la misma moneda
        if otro.moneda != self.moneda:
            raise ValueError("No se pueden sumar monedas distintas")
        # Devuelve un Dinero NUEVO; el original no cambia
        return Dinero(self.monto + otro.monto, self.moneda)

    def multiplicar(self, cantidad: int) -> "Dinero":
        # Multiplica el monto por una cantidad (precio x unidades)
        return Dinero(self.monto * cantidad, self.moneda)

    def formatear(self) -> str:
        # Texto para mostrar en pantalla, por ejemplo "S/ 25.50"
        return f"S/ {self.monto:.2f}"
