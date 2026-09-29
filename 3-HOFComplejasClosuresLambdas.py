from typing import Callable, List, Dict, Any, TypeVar
import time

# Variables de tipo para genericidad en el tipado
T = TypeVar('T')
R = TypeVar('R')

# 1. Pipeline de Mapeo y Filtrado Combinado
def procesar_coleccion(listaElementos: List[T], fn_predicado: Callable[[T], bool], fn_transformacion: Callable[[T], R]) -> List[R]:
    elementosFiltrados = filter(fn_predicado, listaElementos)
    elementosMapeados = map(fn_transformacion, elementosFiltrados)
    return list(elementosMapeados)

# 2. Reductor / Agrupador Personalizado
def agrupar_por(listaDiccionarios: List[Dict[str, Any]], fn_clave: Callable[[Dict[str, Any]], Any]) -> Dict[Any, List[Dict[str, Any]]]:
    diccionarioAgrupado: Dict[Any, List[Dict[str, Any]]] = {}
    for elementoActual in listaDiccionarios:
        claveGenerada = fn_clave(elementoActual)
        if claveGenerada not in diccionarioAgrupado:
            diccionarioAgrupado[claveGenerada] = []
        diccionarioAgrupado[claveGenerada].append(elementoActual)
    return diccionarioAgrupado

# 3. Ejecutor Repetitivo con Estado Accesible
def ejecutar_y_rastrear(fn_tarea: Callable[[], Any], cantidadVeces: int) -> Callable[[], List[Any]]:
    historialResultados: List[Any] = []
    def ejecutarProceso() -> List[Any]:
        nonlocal historialResultados
        if not historialResultados:
            for _ in range(cantidadVeces):
                historialResultados.append(fn_tarea())
        return historialResultados
    return ejecutarProceso

# 4. Compositor de Cadenas de Operaciones
def componer_dos(f: Callable[[Any], Any], g: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def funcionCompuesta(valorInicial: Any) -> Any:
        resultadoIntermedio = g(valorInicial)
        resultadoFinal = f(resultadoIntermedio)
        return resultadoFinal
    return funcionCompuesta

# 5. Decorador / HOF de Profiling y Auditoría
def auditar_ejecucion(fn_objetivo: Callable[..., Any], fn_logger: Callable[[str], None]) -> Callable[..., Any]:
    def envolturaEjecucion(*args, **kwargs) -> Any:
        tiempoInicio: float = time.time()
        resultadoEjecucion = fn_objetivo(*args, **kwargs)
        tiempoFin: float = time.time()
        tiempoTotal: float = tiempoFin - tiempoInicio
        
        mensajeAuditoria: str = f"Auditoría: '{fn_objetivo.__name__}' tardó {tiempoTotal:.6f} segundos."
        fn_logger(mensajeAuditoria)
        
        return resultadoEjecucion
    return envolturaEjecucion


# ==========================================
# PRUEBAS DE EJECUCIÓN (Flujo principal directo)
# ==========================================

print("--- 1. Pipeline de Mapeo y Filtrado ---")
datosIniciales: List[int] = [1, 2, 3, 4, 5, 6]
# Filtra pares y los multiplica por 10
resultadoPipeline = procesar_coleccion(datosIniciales, lambda x: x % 2 == 0, lambda x: x * 10)
print(f"Resultado: {resultadoPipeline}")

print("\n--- 2. Reductor / Agrupador Personalizado ---")
usuariosSistema: List[Dict[str, str]] = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Mara", "rol": "admin"}
]
usuariosAgrupados = agrupar_por(usuariosSistema, lambda u: u["rol"])
print(f"Agrupados por rol: {usuariosAgrupados}")

print("\n--- 3. Ejecutor Repetitivo ---")
# Genera un valor temporal simulando un proceso
rastreadorProceso = ejecutar_y_rastrear(lambda: time.time(), 3)
print(f"Historial de ejecuciones: {rastreadorProceso()}")

print("\n--- 4. Compositor de Cadenas ---")
# Primero suma 5, luego multiplica por 2: f(g(x)) = (x + 5) * 2
operacionCombinada = componer_dos(lambda x: x * 2, lambda x: x + 5)
print(f"Resultado de (10 + 5) * 2: {operacionCombinada(10)}")

print("\n--- 5. Decorador / Auditoría ---")
def calculoPesado(limite: int) -> int:
    return sum([i for i in range(limite)])

funcionAuditada = auditar_ejecucion(calculoPesado, lambda mensaje: print(f"[LOG DEL SISTEMA] {mensaje}"))
print(f"Resultado del cálculo: {funcionAuditada(1000000)}")