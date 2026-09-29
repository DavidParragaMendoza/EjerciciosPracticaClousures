from typing import Callable, List, Dict, Any, TypeVar

T = TypeVar('T')
R = TypeVar('R')

# Constante para probar el límite de la memoria caché
MAXIMOCACHE_DEFAULT: int = 3

# 1. Validador Compuesto de Reglas de Negocio
def crear_validador_múltiple(*lambdas_criterios: Callable[[Any], bool]) -> Callable[[Any], bool]:
    def evaluarObjeto(objetoEvaluar: Any) -> bool:
        # all() aplica cada lambda al objeto y retorna True solo si todas se cumplen
        for criterioActual in lambdas_criterios:
            if not criterioActual(objetoEvaluar):
                return False
        return True
    return evaluarObjeto

# 2. Caché con Expiración o Tamaño Máximo (Memoización Profesional)
def memoizar_avanzado(fn_costosa: Callable[[Any], Any], max_items: int = MAXIMOCACHE_DEFAULT) -> Callable[[Any], Any]:
    memoriaPrivada: Dict[Any, Any] = {}
    ordenClaves: List[Any] = []
    
    def ejecutarConCache(argumentoEntrada: Any) -> Any:
        nonlocal memoriaPrivada, ordenClaves
        
        if argumentoEntrada in memoriaPrivada:
            return memoriaPrivada[argumentoEntrada]
            
        resultadoCalculado = fn_costosa(argumentoEntrada)
        
        if len(memoriaPrivada) >= max_items:
            claveAntigua = ordenClaves.pop(0)
            del memoriaPrivada[claveAntigua]
            
        memoriaPrivada[argumentoEntrada] = resultadoCalculado
        ordenClaves.append(argumentoEntrada)
        
        return resultadoCalculado
    return ejecutarConCache

# 3. Motor de Pipeline Secuencial (Currying / Middleware)
def crear_pipeline(*funciones_transformacion: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def inyectarDatoInicial(datoInicial: Any) -> Any:
        datoProcesado = datoInicial
        for funcionActual in funciones_transformacion:
            datoProcesado = funcionActual(datoProcesado)
        return datoProcesado
    return inyectarDatoInicial

# 4. Sistema Pub/Sub (Event Listener con HOFs y Closures)
def crear_sistema_eventos() -> Dict[str, Callable]:
    listaSuscriptores: List[Callable[[Any], None]] = []
    
    def registrarSuscriptor(fn_suscriptor: Callable[[Any], None]) -> None:
        nonlocal listaSuscriptores
        listaSuscriptores.append(fn_suscriptor)
        
    def notificarEvento(datosEvento: Any) -> int:
        for suscriptor in listaSuscriptores:
            suscriptor(datosEvento)
        return len(listaSuscriptores)
        
    # Retorna un diccionario actuando como un gestor (similar a crear_cuenta_bancaria)
    return {
        "registrar": registrarSuscriptor,
        "emitir": notificarEvento
    }

# 5. Mini-Query Engine sobre Listas de Objetos
def crear_consultor(campo: str) -> Callable[[Callable[[Any], bool]], Callable[[List[Dict[str, Any]]], List[Dict[str, Any]]]]:
    def inyectarCondicion(lambda_condicion: Callable[[Any], bool]) -> Callable[[List[Dict[str, Any]]], List[Dict[str, Any]]]:
        def aplicarFiltro(listaObjetos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
            elementosFiltrados = filter(lambda obj: lambda_condicion(obj.get(campo)), listaObjetos)
            return list(elementosFiltrados)
        return aplicarFiltro
    return inyectarCondicion


# ==========================================
# PRUEBAS DE EJECUCIÓN 
# ==========================================

print("--- 1. Validador Compuesto ---")
validadorUsuario = crear_validador_múltiple(
    lambda u: u.get("edad", 0) >= 18,
    lambda u: u.get("rol") == "admin",
    lambda u: u.get("activo") is True
)
usuarioA: Dict[str, Any] = {"edad": 20, "rol": "admin", "activo": True}
usuarioB: Dict[str, Any] = {"edad": 17, "rol": "admin", "activo": True}
print(f"Usuario A válido: {validadorUsuario(usuarioA)}")
print(f"Usuario B válido: {validadorUsuario(usuarioB)}")

print("\n--- 2. Caché con Tamaño Máximo ---")
calculoCacheado = memoizar_avanzado(lambda x: x ** 2, 2)
print(f"Cálculo de 4: {calculoCacheado(4)}") # Se guarda
print(f"Cálculo de 5: {calculoCacheado(5)}") # Se guarda
print(f"Cálculo de 6: {calculoCacheado(6)}") # Expulsa al 4 (FIFO)
print("Se ejecutó correctamente limitando el crecimiento interno.")

print("\n--- 3. Motor de Pipeline Secuencial ---")
procesarTexto = crear_pipeline(
    lambda txt: txt.strip(),
    lambda txt: txt.lower(),
    lambda txt: txt.replace(" ", "_")
)
print(f"Pipeline de texto: {procesarTexto('   HOLA Mundo  ')}")

print("\n--- 4. Sistema Pub/Sub ---")
gestorEventos = crear_sistema_eventos()
gestorEventos["registrar"](lambda msg: print(f"Servicio Email recibió: {msg}"))
gestorEventos["registrar"](lambda msg: print(f"Servicio Logger recibió: {msg}"))
totalNotificados = gestorEventos["emitir"]({"tipo": "ALERTA", "codigo": 404})
print(f"Total de suscriptores notificados: {totalNotificados}")

print("\n--- 5. Mini-Query Engine ---")
consultorPrecio = crear_consultor("precio")
# Inyectamos la lambda para que evalúe si el precio es mayor a 100
filtroPrecioAlto = consultorPrecio(lambda p: p is not None and p > 100.0)

productosInventario: List[Dict[str, Any]] = [
    {"nombre": "Teclado", "precio": 150.0},
    {"nombre": "Mouse", "precio": 25.0},
    {"nombre": "Monitor", "precio": 300.0}
]
print(f"Productos caros: {filtroPrecioAlto(productosInventario)}")