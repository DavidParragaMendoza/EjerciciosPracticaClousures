from typing import Any, Callable, Dict, List


def memoizar_avanzado(
    fn_costosa: Callable[[Any], Any], max_items: int
) -> Callable[[Any], Any]:
    memoria_privada: Dict[Any, Any] = {}
    orden_claves: List[Any] = []

    def ejecutar_con_cache(argumento: Any) -> Any:
        if argumento in memoria_privada:
            return memoria_privada[argumento]
        if len(memoria_privada) >= max_items:
            clave_antigua = orden_claves.pop(0)
            del memoria_privada[clave_antigua]
        memoria_privada[argumento] = fn_costosa(argumento)
        orden_claves.append(argumento)
        return memoria_privada[argumento]

    return ejecutar_con_cache


calculo_cacheado = memoizar_avanzado(lambda numero: numero ** 2, 2)
print(calculo_cacheado(4))
print(calculo_cacheado(5))
print(calculo_cacheado(6))
