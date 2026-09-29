<div align="center">

# 🧪 Taller de Programación Funcional

### Python · HOFs · Lambdas · Closures

<img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.14">
<img src="https://img.shields.io/badge/Ejercicios-20-2EA44F?style=for-the-badge" alt="20 ejercicios">
<img src="https://img.shields.io/badge/Niveles-4-8250DF?style=for-the-badge" alt="4 niveles">

**Una colección práctica para aprender a combinar funciones de orden superior,**
**lambdas y closures en Python.**

</div>

> [!IMPORTANT]
> Cada mini-ejercicio está separado en su propio archivo `.py` e incluye una prueba de ejecución con `print()`.

## 🧭 Contenido

- [🎯 Objetivo](#-objetivo)
- [🗂️ Niveles](#️-niveles)
- [🧠 Ejercicios](#-ejercicios)
- [📫 Contacto](#-contacto)

## 🎯 Objetivo

Este proyecto presenta una progresión desde closures sencillos hasta patrones funcionales de arquitectura. La idea central es inyectar comportamientos mediante funciones y lambdas, encapsular estado sin exponerlo directamente y componer soluciones pequeñas, reutilizables y fáciles de probar.

> [!TIP]
> Puedes ejecutar los ejercicios en cualquier orden. Cada archivo funciona de manera independiente y muestra su resultado en la consola.

## 🗂️ Niveles

| Nivel | Tema | Enfoque |
|:---:|---|---|
| 🟢 **1** | [Closures con inyección](nivel1) | Comportamientos dinámicos con lambdas |
| 🟠 **2** | [Estado encapsulado](nivel2) | `nonlocal` y memoria privada |
| 🔵 **3** | [HOFs combinadas](nivel3) | `filter`, `map`, composición y auditoría |
| 🟣 **4** | [Arquitectura funcional](nivel4) | Memoización, eventos y consultas |

## 🧠 Ejercicios

### 🟢 Nivel 1 · Closures con Inyección de Comportamiento

1. **Generador de formateadores:** [`1-generador_formateadores.py`](nivel1/1-generador_formateadores.py) transforma un texto con una lambda y le agrega un prefijo configurable.
2. **Multiplicador paramétrico:** [`2-multiplicador_parametrico.py`](nivel1/2-multiplicador_parametrico.py) encapsula un factor y permite aplicar distintas operaciones.
3. **Calculador de descuentos:** [`3-calculador_descuentos.py`](nivel1/3-calculador_descuentos.py) decide dinámicamente si aplica un descuento.
4. **Generador de seriales:** [`4-generador_seriales.py`](nivel1/4-generador_seriales.py) transforma nombres usando un patrón recibido.
5. **Conversor de divisas:** [`5-conversor_divisas.py`](nivel1/5-conversor_divisas.py) convierte montos y calcula una comisión adicional.

<details>
<summary>💡 Ejemplo explicado</summary>

El ejercicio [`1-generador_formateadores.py`](nivel1/1-generador_formateadores.py) demuestra cómo una función recibe un comportamiento mediante una lambda y devuelve un closure. `crear_formateador` guarda el prefijo y la transformación; luego, la función interna transforma el texto y concatena ambos valores. Así se obtiene un formateador reutilizable sin repetir la lógica.

</details>

### 🟠 Nivel 2 · Estado Encapsulado Avanzado

1. **Contador ponderado:** [`1-contador_ponderado.py`](nivel2/1-contador_ponderado.py) conserva una cuenta privada y delega el incremento.
2. **Acumulador validado:** [`2-acumulador_validado.py`](nivel2/2-acumulador_validado.py) suma solo los valores aceptados por un criterio.
3. **Promediador filtrado:** [`3-promediador_filtrado.py`](nivel2/3-promediador_filtrado.py) descarta valores atípicos antes de calcular el promedio.
4. **Limitador de tasa:** [`4-limitador_tasa.py`](nivel2/4-limitador_tasa.py) controla ejecuciones y dispara una alerta al superar el límite.
5. **Interruptor múltiple:** [`5-interruptor_multiple.py`](nivel2/5-interruptor_multiple.py) recorre cíclicamente una lista de estados.

<details>
<summary>💡 Ejemplo explicado</summary>

El ejercicio [`2-acumulador_validado.py`](nivel2/2-acumulador_validado.py) muestra cómo un closure conserva estado privado entre llamadas. `total_acumulado` solo cambia cuando el valor cumple el criterio enviado como lambda; los valores rechazados no alteran el total y los válidos quedan disponibles para la siguiente llamada.

</details>

### 🔵 Nivel 3 · HOFs, Closures y Lambdas

1. **Pipeline de mapeo y filtrado:** [`1-pipeline_mapeo_filtrado.py`](nivel3/1-pipeline_mapeo_filtrado.py) combina `filter` y `map`.
2. **Agrupador personalizado:** [`2-agrupar_por.py`](nivel3/2-agrupar_por.py) organiza diccionarios usando una función que calcula la clave.
3. **Ejecutor repetitivo:** [`3-ejecutor_repetitivo.py`](nivel3/3-ejecutor_repetitivo.py) conserva el historial de varias ejecuciones.
4. **Compositor de operaciones:** [`4-compositor_operaciones.py`](nivel3/4-compositor_operaciones.py) aplica la composición `f(g(x))`.
5. **Auditoría y profiling:** [`5-auditoria_profiling.py`](nivel3/5-auditoria_profiling.py) mide la duración y envía el informe a un logger.

<details>
<summary>💡 Ejemplo explicado</summary>

El ejercicio [`1-pipeline_mapeo_filtrado.py`](nivel3/1-pipeline_mapeo_filtrado.py) combina `filter`, que selecciona elementos mediante un predicado, y `map`, que transforma los elementos aceptados. Como ambas operaciones se reciben como argumentos, el pipeline puede reutilizarse con diferentes reglas sin cambiar su estructura.

</details>

### 🟣 Nivel 4 · Arquitectura Funcional

1. **Validador compuesto:** [`1-validador_compuesto.py`](nivel4/1-validador_compuesto.py) exige que se cumplan todos los criterios de negocio.
2. **Memoización avanzada:** [`2-memoizacion_avanzada.py`](nivel4/2-memoizacion_avanzada.py) limita una caché con política FIFO.
3. **Pipeline secuencial:** [`3-pipeline_secuencial.py`](nivel4/3-pipeline_secuencial.py) encadena transformaciones en orden.
4. **Sistema Pub/Sub:** [`4-sistema_pubsub.py`](nivel4/4-sistema_pubsub.py) registra suscriptores y notifica eventos.
5. **Mini-query engine:** [`5-mini_query_engine.py`](nivel4/5-mini_query_engine.py) genera filtros dinámicos para listas de diccionarios.

<details>
<summary>💡 Ejemplo explicado</summary>

El ejercicio [`2-memoizacion_avanzada.py`](nivel4/2-memoizacion_avanzada.py) evita repetir cálculos costosos guardando resultados en una caché privada. Cuando la capacidad máxima se alcanza, elimina el resultado más antiguo mediante una política FIFO. De esta forma, reutiliza resultados conocidos sin permitir que la memoria crezca indefinidamente.

</details>


## 📫 Contacto

- 💼 **LinkedIn:** [David Parraga Mendoza](https://www.linkedin.com/in/davidparragamendoza/)
- 𝕏 **X:** [@DavidParragaMen](https://x.com/DavidParragaMen)

<div align="center">

✨ **Gracias por visitar este proyecto** ✨

</div>
