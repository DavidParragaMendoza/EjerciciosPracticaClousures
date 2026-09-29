from typing import Callable


def crear_generador_sufijos(patron_lambda: Callable[[str], str]) -> Callable[[str], str]:
    def transformar_nombre_archivo(nombre_archivo: str) -> str:
        return patron_lambda(nombre_archivo)

    return transformar_nombre_archivo


generador_version = crear_generador_sufijos(lambda nombre: f"{nombre}_v2.0_FINAL")
print(generador_version("documento_arquitectura"))
