## Análisis cola M/M/1/K

##  Objetivos

* Implementar un modelo de colas **M/M/1/K/∞** en 
* Calcular métricas clave del sistema tanto de forma **matemática** como mediante **simulación**.
* Comparar los resultados obtenidos para validar el modelo computacional.

#

Se calcularon las métricas teóricas mediante el modelo matemático y se comprobaron mediante simulación en netLogo y en mesa mesiante Python.


##  Requisitos

Antes de ejecutar el programa, debes tener instalado en python y el paquete **NumPy**.

## Ejecución

Ejecuta el archivo principal:

```bash
python3 mm1k_simulacion.py
```

## Ejemplo de salida

Resultados obtenidos al correr la simulación:

| Métrica                         | Valor aproximado  |
| ------------------------------- | ----------------- |
| NS (número medio en el sistema) | 5.52              |
| Nw (número medio en la cola)    | 4.53              |
| TS (tiempo medio en el sistema) | 2.79 min          |
| Tw (tiempo medio en la cola)    | 2.45 min          |
| λe (tasa efectiva de llegada)   | 1.98 clientes/min |
| Clientes bloqueados             | 368               |
| Clientes totales simulados      | 39,936            |

##  Conclusión

El modelo matemático y la simulación muestran valores muy cercanos, validando la correcta implementación del sistema M/M/1/K/ Infinito en Python.



