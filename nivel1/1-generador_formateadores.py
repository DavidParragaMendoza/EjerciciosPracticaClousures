from typing import Callable


def crear_formateador(prefijo: str, fn_transformacion: Callable[[str], str]) -> Callable[[str], str]:
    def aplicar_formato(texto_base: str) -> str:
        return f"{prefijo}{fn_transformacion(texto_base)}"

    return aplicar_formato


formateador_log = crear_formateador("[SISTEMA] - ", lambda texto: texto.upper())
print(formateador_log("inicio de sesión exitoso"))
