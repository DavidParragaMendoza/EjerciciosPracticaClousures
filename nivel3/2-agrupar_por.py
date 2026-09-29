from typing import Any, Callable, Dict, List


def agrupar_por(
    lista: List[Dict[str, Any]],
    fn_clave: Callable[[Dict[str, Any]], Any],
) -> Dict[Any, List[Dict[str, Any]]]:
    resultado: Dict[Any, List[Dict[str, Any]]] = {}
    for elemento in lista:
        resultado.setdefault(fn_clave(elemento), []).append(elemento)
    return resultado


usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Mara", "rol": "admin"},
]
print(f"Agrupados por rol: {agrupar_por(usuarios, lambda usuario: usuario['rol'])}")
