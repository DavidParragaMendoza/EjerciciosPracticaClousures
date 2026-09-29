# Taller de Programación Funcional en Python

Este proyecto reúne ejercicios de funciones de orden superior (HOF), lambdas y closures. Cada nivel está organizado en una carpeta y cada mini-ejercicio tiene su propio archivo `.py` con una prueba de ejecución mediante `print()`.

## Estructura

- `nivel1`: Closures con inyección de comportamiento.
- `nivel2`: Estado encapsulado con `nonlocal`.
- `nivel3`: HOFs combinadas con closures y lambdas.
- `nivel4`: Patrones avanzados de arquitectura funcional.

## Nivel 1: Closures con Inyección de Comportamiento

1. **Generador de formateadores:** `1-generador_formateadores.py` crea una función que transforma un texto con una lambda y le agrega un prefijo configurable.
2. **Multiplicador paramétrico:** `2-multiplicador_parametrico.py` encapsula un factor y permite aplicar distintas operaciones sobre un valor recibido.
3. **Calculador de descuentos:** `3-calculador_descuentos.py` evalúa una regla dinámica para decidir si aplica un descuento prefijado.
4. **Generador de seriales:** `4-generador_seriales.py` transforma nombres de archivos usando un patrón inyectado como lambda.
5. **Conversor de divisas:** `5-conversor_divisas.py` convierte un monto y calcula una comisión mediante una función de margen.

## Nivel 2: Estado Encapsulado Avanzado

1. **Contador ponderado:** `1-contador_ponderado.py` mantiene una cuenta privada y delega el incremento en una función recibida.
2. **Acumulador validado:** `2-acumulador_validado.py` suma únicamente los valores que cumplen el criterio de aceptación.
3. **Promediador filtrado:** `3-promediador_filtrado.py` conserva suma y cantidad en un closure y descarta valores atípicos antes de calcular el promedio.
4. **Limitador de tasa:** `4-limitador_tasa.py` controla el número de ejecuciones y llama a una función de alerta cuando se supera el límite.
5. **Interruptor múltiple:** `5-interruptor_multiple.py` encapsula un índice y recorre cíclicamente una lista de estados.

## Nivel 3: HOFs, Closures y Lambdas

1. **Pipeline de mapeo y filtrado:** `1-pipeline_mapeo_filtrado.py` combina `filter` y `map` para seleccionar y transformar elementos.
2. **Agrupador personalizado:** `2-agrupar_por.py` organiza diccionarios en grupos usando una función que calcula la clave.
3. **Ejecutor repetitivo:** `3-ejecutor_repetitivo.py` ejecuta una tarea varias veces y conserva el historial en un closure accesible.
4. **Compositor de operaciones:** `4-compositor_operaciones.py` devuelve una función que aplica la composición `f(g(x))`.
5. **Auditoría y profiling:** `5-auditoria_profiling.py` mide la duración de una función y envía el informe a un logger inyectado.

## Nivel 4: Arquitectura Funcional

1. **Validador compuesto:** `1-validador_compuesto.py` devuelve verdadero solo cuando el objeto cumple todos los criterios de negocio.
2. **Memoización avanzada:** `2-memoizacion_avanzada.py` almacena resultados y limita la caché mediante una política FIFO.
3. **Pipeline secuencial:** `3-pipeline_secuencial.py` crea una función que encadena transformaciones en el orden recibido.
4. **Sistema Pub/Sub:** `4-sistema_pubsub.py` permite registrar suscriptores y notificarles eventos desde un gestor con estado privado.
5. **Mini-query engine:** `5-mini_query_engine.py` genera filtros dinámicos para consultar listas de diccionarios por un campo y una condición.

## Ejecución

Desde la carpeta principal se puede ejecutar cualquier ejercicio con:

```bash
python nivel1/1-generador_formateadores.py
```

Los archivos originales `1-...py` a `4-...py` se conservan como referencia de los ejercicios completos por nivel.
