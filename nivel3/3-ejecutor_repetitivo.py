from typing import Any, Callable, List
import time


def ejecutar_y_rastrear(fn_tarea: Callable[[], Any], n: int) -> Callable[[], List[Any]]:
    historial_resultados: List[Any] = []

    def ejecutar_proceso() -> List[Any]:
        if not historial_resultados:
            for _ in range(n):
                historial_resultados.append(fn_tarea())
        return historial_resultados

    return ejecutar_proceso


rastreador = ejecutar_y_rastrear(lambda: time.time(), 3)
print(f"Historial de ejecuciones: {rastreador()}")
