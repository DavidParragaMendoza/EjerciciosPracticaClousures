from typing import Callable, List

# Constante para probar el límite de peticiones
LIMITEPETICIONES: int = 3

# 1. Contador Ponderado
def crear_contador_paso(fn_paso: Callable[[int], int]) -> Callable[[], int]:
    cuentaActual: int = 0
    def incrementar() -> int:
        nonlocal cuentaActual
        cuentaActual = fn_paso(cuentaActual)
        return cuentaActual
    return incrementar

# 2. Acumulador con Filtro de Aceptación
def crear_acumulador_validado(criterio_lambda: Callable[[float], bool]) -> Callable[[float], float]:
    totalAcumulado: float = 0.0
    def sumarValido(valorIngresado: float) -> float:
        nonlocal totalAcumulado
        if criterio_lambda(valorIngresado):
            totalAcumulado += valorIngresado
        return totalAcumulado
    return sumarValido

# 3. Promediador con Eliminación de Valores Extremos
def crear_promediador_filtrado(filtro_ruido_lambda: Callable[[float], bool]) -> Callable[[float], float]:
    sumaTotal: float = 0.0
    cantidadElementos: int = 0
    def calcularPromedio(valorNuevo: float) -> float:
        nonlocal sumaTotal, cantidadElementos
        # Si la lambda devuelve True, significa que es un valor atípico y se descarta
        if not filtro_ruido_lambda(valorNuevo):
            sumaTotal += valorNuevo
            cantidadElementos += 1
        promedioCalculado: float = sumaTotal / cantidadElementos if cantidadElementos > 0 else 0.0
        return promedioCalculado
    return calcularPromedio

# 4. Limitador de Tasa Inteligente (Rate Limiter con Reset)
def crear_limitador_avanzado(max_intentos: int, fn_alerta: Callable[[int], str]) -> Callable[[], str]:
    ejecucionesPrivadas: int = 0
    def ejecutarPeticion() -> str:
        nonlocal ejecucionesPrivadas
        if ejecucionesPrivadas >= max_intentos:
            mensajeAlerta: str = fn_alerta(ejecucionesPrivadas)
            return mensajeAlerta
        ejecucionesPrivadas += 1
        return f"Ejecución exitosa. Intento {ejecucionesPrivadas} de {max_intentos}."
    return ejecutarPeticion

# 5. Interruptor Múltiple (Máquina de Estados Ligera)
def crear_conmutador(lista_estados: List[str]) -> Callable[[], str]:
    indiceActual: int = -1
    def alternarEstado() -> str:
        nonlocal indiceActual
        indiceActual = (indiceActual + 1) % len(lista_estados)
        estadoSeleccionado: str = lista_estados[indiceActual]
        return estadoSeleccionado
    return alternarEstado


# ==========================================
# PRUEBAS DE EJECUCIÓN
# ==========================================
print("--- 1. Contador Ponderado ---")
contadorPares = crear_contador_paso(lambda cuenta: cuenta + 2)
print(contadorPares())
print(contadorPares())

print("\n--- 2. Acumulador con Filtro ---")
acumuladorPositivos = crear_acumulador_validado(lambda valor: valor > 0.0)
print(f"Acumulado: {acumuladorPositivos(10.0)}")
print(f"Acumulado (Ignorando -5): {acumuladorPositivos(-5.0)}")
print(f"Acumulado: {acumuladorPositivos(20.0)}")

print("\n--- 3. Promediador Filtrado ---")
promediadorNormal = crear_promediador_filtrado(lambda valor: valor > 100.0)
print(f"Promedio: {promediadorNormal(10.0)}")
print(f"Promedio (Ignorando 150): {promediadorNormal(150.0)}")
print(f"Promedio: {promediadorNormal(20.0)}")

print("\n--- 4. Limitador de Tasa ---")
limitadorApi = crear_limitador_avanzado(LIMITEPETICIONES, lambda intentos: f"¡ALERTA! Límite superado tras {intentos} intentos.")
print(limitadorApi())
print(limitadorApi())
print(limitadorApi())
print(limitadorApi()) # Se dispara la lambda de alerta

print("\n--- 5. Interruptor Múltiple ---")
semaforo = crear_conmutador(["VERDE", "AMARILLO", "ROJO"])
print(semaforo())
print(semaforo())
print(semaforo())
print(semaforo()) # Vuelve a iniciar el ciclo