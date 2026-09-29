from typing import Any, Callable


def crear_validador_multiple(*criterios: Callable[[Any], bool]) -> Callable[[Any], bool]:
    def evaluar(objeto: Any) -> bool:
        return all(criterio(objeto) for criterio in criterios)

    return evaluar


validador_usuario = crear_validador_multiple(
    lambda usuario: usuario.get("edad", 0) >= 18,
    lambda usuario: usuario.get("rol") == "admin",
    lambda usuario: usuario.get("activo") is True,
)
print(validador_usuario({"edad": 20, "rol": "admin", "activo": True}))
print(validador_usuario({"edad": 17, "rol": "admin", "activo": True}))
