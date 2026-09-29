from typing import Callable


def crear_limitador_avanzado(max_intentos: int, fn_alerta: Callable[[int], str]) -> Callable[[], str]:
    ejecuciones_privadas = 0

    def ejecutar_peticion() -> str:
        nonlocal ejecuciones_privadas
        if ejecuciones_privadas >= max_intentos:
            return fn_alerta(ejecuciones_privadas)
        ejecuciones_privadas += 1
        return f"Ejecución exitosa. Intento {ejecuciones_privadas} de {max_intentos}."

    return ejecutar_peticion


limitador_api = crear_limitador_avanzado(
    3, lambda intentos: f"¡ALERTA! Límite superado tras {intentos} intentos."
)
for _ in range(4):
    print(limitador_api())
