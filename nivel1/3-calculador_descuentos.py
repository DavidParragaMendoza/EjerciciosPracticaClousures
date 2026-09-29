from typing import Callable

DESCUENTO_PREFIJADO: float = 0.15


def crear_descuento_dinamico(regla_condicional_lambda: Callable[[float], bool]) -> Callable[[float], float]:
    def evaluar_precio(precio_base: float) -> float:
        if regla_condicional_lambda(precio_base):
            return precio_base - (precio_base * DESCUENTO_PREFIJADO)
        return precio_base

    return evaluar_precio


descuento_feriado = crear_descuento_dinamico(lambda precio: precio > 50.0)
print(f"Precio $100 (aplica descuento): ${descuento_feriado(100.0)}")
print(f"Precio $30 (no aplica): ${descuento_feriado(30.0)}")
