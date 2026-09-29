from typing import Callable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def procesar_coleccion(
    lista: List[T],
    fn_predicado: Callable[[T], bool],
    fn_transformacion: Callable[[T], R],
) -> List[R]:
    return list(map(fn_transformacion, filter(fn_predicado, lista)))


datos = [1, 2, 3, 4, 5, 6]
resultado = procesar_coleccion(datos, lambda x: x % 2 == 0, lambda x: x * 10)
print(f"Resultado: {resultado}")
