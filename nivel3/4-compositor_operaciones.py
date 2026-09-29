from typing import Any, Callable


def componer_dos(f: Callable[[Any], Any], g: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def funcion_compuesta(valor_inicial: Any) -> Any:
        return f(g(valor_inicial))

    return funcion_compuesta


operacion_combinada = componer_dos(lambda x: x * 2, lambda x: x + 5)
print(f"Resultado de (10 + 5) * 2: {operacion_combinada(10)}")
