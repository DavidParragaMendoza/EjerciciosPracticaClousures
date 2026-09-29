from typing import Callable


def crear_contador_paso(fn_paso: Callable[[int], int]) -> Callable[[], int]:
    cuenta_actual = 0

    def incrementar() -> int:
        nonlocal cuenta_actual
        cuenta_actual = fn_paso(cuenta_actual)
        return cuenta_actual

    return incrementar


contador_pares = crear_contador_paso(lambda cuenta: cuenta + 2)
print(contador_pares())
print(contador_pares())
