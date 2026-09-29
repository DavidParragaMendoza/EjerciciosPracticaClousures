from typing import Callable

# Constante para el ejercicio de descuento dinámico
DESCUENTOPREFIJADO: float = 0.15  # Representa un 15% de descuento

# 1. Generador de Formateadores con Transformación
def crear_formateador(prefijo: str, fn_transformacion: Callable[[str], str]) -> Callable[[str], str]:
    def aplicarFormato(textoBase: str) -> str:
        textoTransformado: str = fn_transformacion(textoBase)
        textoFinal: str = f"{prefijo}{textoTransformado}"
        return textoFinal
    return aplicarFormato

# 2. Multiplicador Paramétrico con Mapeo
def crear_operador(factor: float, operacion_lambda: Callable[[float, float], float]) -> Callable[[float], float]:
    def ejecutarOperacion(valorBase: float) -> float:
        resultadoOperacion: float = operacion_lambda(valorBase, factor)
        return resultadoOperacion
    return ejecutarOperacion

# 3. Calculador de Descuentos con Regla Dinámica
def crear_descuento_dinamico(regla_condicional_lambda: Callable[[float], bool]) -> Callable[[float], float]:
    def evaluarPrecio(precioBase: float) -> float:
        if regla_condicional_lambda(precioBase):
            precioFinal: float = precioBase - (precioBase * DESCUENTOPREFIJADO)
            return precioFinal
        return precioBase
    return evaluarPrecio

# 4. Generador de Seriales / Nombres Únicos
def crear_generador_sufijos(patron_lambda: Callable[[str], str]) -> Callable[[str], str]:
    def transformarNombreArchivo(nombreArchivo: str) -> str:
        nombreNuevo: str = patron_lambda(nombreArchivo)
        return nombreNuevo
    return transformarNombreArchivo

# 5. Conversor de Divisas con Margen
def crear_conversor(tasa: float, margen_lambda: Callable[[float], float]) -> Callable[[float], float]:
    def convertirMonto(montoBase: float) -> float:
        montoConvertido: float = montoBase * tasa
        comisionAdicional: float = margen_lambda(montoConvertido)
        montoFinal: float = montoConvertido + comisionAdicional
        return montoFinal
    return convertirMonto


# PRUEBAS DE EJECUCIÓN (Verificación con print)


print("--- 1. Generador de Formateadores ---")
formateadorLog = crear_formateador("[SISTEMA] - ", lambda texto: texto.upper())
print(formateadorLog("inicio de sesión exitoso"))

print("\n--- 2. Multiplicador Paramétrico ---")
operadorPotencia = crear_operador(3.0, lambda base, factor: base ** factor)
print(f"2 elevado al cubo: {operadorPotencia(2.0)}")

print("\n--- 3. Calculador de Descuentos ---")
descuentoFeriado = crear_descuento_dinamico(lambda precio: precio > 50.0)
print(f"Precio $100 (Aplica descuento): ${descuentoFeriado(100.0)}")
print(f"Precio $30 (No aplica): ${descuentoFeriado(30.0)}")

print("\n--- 4. Generador de Seriales ---")
generadorVersion = crear_generador_sufijos(lambda nombre: f"{nombre}_v2.0_FINAL")
print(generadorVersion("documento_arquitectura"))

print("\n--- 5. Conversor de Divisas ---")
conversorEuros = crear_conversor(0.92, lambda monto: monto * 0.05) # 5% de comisión
print(f"100 USD a Euros (incluyendo comisión): €{conversorEuros(100.0)}")