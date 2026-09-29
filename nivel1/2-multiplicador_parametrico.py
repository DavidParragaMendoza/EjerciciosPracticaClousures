from typing import Callable


def crear_operador(factor: float, operacion_lambda: Callable[[float, float], float]) -> Callable[[float], float]:
    def ejecutar_operacion(valor_base: float) -> float:
        return operacion_lambda(valor_base, factor)

    return ejecutar_operacion


operador_potencia = crear_operador(3.0, lambda base, factor: base ** factor)
print(f"2 elevado al cubo: {operador_potencia(2.0)}")
