from typing import Callable


def crear_acumulador_validado(criterio_lambda: Callable[[float], bool]) -> Callable[[float], float]:
    total_acumulado = 0.0

    def sumar_valido(valor_ingresado: float) -> float:
        nonlocal total_acumulado
        if criterio_lambda(valor_ingresado):
            total_acumulado += valor_ingresado
        return total_acumulado

    return sumar_valido


acumulador_positivos = crear_acumulador_validado(lambda valor: valor > 0.0)
print(f"Acumulado: {acumulador_positivos(10.0)}")
print(f"Acumulado (ignorando -5): {acumulador_positivos(-5.0)}")
print(f"Acumulado: {acumulador_positivos(20.0)}")
