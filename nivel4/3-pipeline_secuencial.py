from typing import Any, Callable


def crear_pipeline(*funciones: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def procesar(dato_inicial: Any) -> Any:
        dato = dato_inicial
        for funcion in funciones:
            dato = funcion(dato)
        return dato

    return procesar


procesar_texto = crear_pipeline(
    lambda texto: texto.strip(),
    lambda texto: texto.lower(),
    lambda texto: texto.replace(" ", "_"),
)
print(procesar_texto("   HOLA Mundo  "))
