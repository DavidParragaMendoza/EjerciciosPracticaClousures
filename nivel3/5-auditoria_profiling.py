from typing import Any, Callable
import time


def auditar_ejecucion(
    fn_objetivo: Callable[..., Any], fn_logger: Callable[[str], None]
) -> Callable[..., Any]:
    def envoltura(*args: Any, **kwargs: Any) -> Any:
        inicio = time.time()
        resultado = fn_objetivo(*args, **kwargs)
        duracion = time.time() - inicio
        fn_logger(f"Auditoría: '{fn_objetivo.__name__}' tardó {duracion:.6f} segundos.")
        return resultado

    return envoltura


def calculo_pesado(limite: int) -> int:
    return sum(i for i in range(limite))


funcion_auditada = auditar_ejecucion(
    calculo_pesado, lambda mensaje: print(f"[LOG DEL SISTEMA] {mensaje}")
)
print(f"Resultado del cálculo: {funcion_auditada(1_000_000)}")
