from typing import Callable, List


def crear_conmutador(lista_estados: List[str]) -> Callable[[], str]:
    indice_actual = -1

    def alternar_estado() -> str:
        nonlocal indice_actual
        indice_actual = (indice_actual + 1) % len(lista_estados)
        return lista_estados[indice_actual]

    return alternar_estado


semaforo = crear_conmutador(["VERDE", "AMARILLO", "ROJO"])
for _ in range(4):
    print(semaforo())
