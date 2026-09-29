from typing import Callable


def crear_promediador_filtrado(filtro_ruido_lambda: Callable[[float], bool]) -> Callable[[float], float]:
    suma_total = 0.0
    cantidad_elementos = 0

    def calcular_promedio(valor_nuevo: float) -> float:
        nonlocal suma_total, cantidad_elementos
        if not filtro_ruido_lambda(valor_nuevo):
            suma_total += valor_nuevo
            cantidad_elementos += 1
        return suma_total / cantidad_elementos if cantidad_elementos > 0 else 0.0

    return calcular_promedio


promediador_normal = crear_promediador_filtrado(lambda valor: valor > 100.0)
print(f"Promedio: {promediador_normal(10.0)}")
print(f"Promedio (ignorando 150): {promediador_normal(150.0)}")
print(f"Promedio: {promediador_normal(20.0)}")
