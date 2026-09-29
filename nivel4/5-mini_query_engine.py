from typing import Any, Callable, Dict, List


def crear_consultor(campo: str) -> Callable[[Callable[[Any], bool]], Callable[[List[Dict[str, Any]]], List[Dict[str, Any]]]]:
    def crear_filtro(condicion: Callable[[Any], bool]) -> Callable[[List[Dict[str, Any]]], List[Dict[str, Any]]]:
        def aplicar_filtro(elementos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
            return list(filter(lambda elemento: condicion(elemento.get(campo)), elementos))

        return aplicar_filtro

    return crear_filtro


productos = [
    {"nombre": "Teclado", "precio": 150.0},
    {"nombre": "Mouse", "precio": 25.0},
    {"nombre": "Monitor", "precio": 300.0},
]
filtro_caros = crear_consultor("precio")(lambda precio: precio is not None and precio > 100.0)
print(f"Productos caros: {filtro_caros(productos)}")
