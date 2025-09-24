Aquí tienes el **README final** que resume todo tu trabajo, con objetivos, explicación, instrucciones y un ejemplo de salida de la simulación en Python con **NumPy**:

---

# 📄 Simulación M/M/1/K

## 🎯 Objetivos

* Implementar un modelo de colas **M/M/1/K/∞** en Python.
* Calcular métricas clave del sistema tanto de forma **matemática** como mediante **simulación**.
* Comparar los resultados obtenidos para validar el modelo computacional.

## 📝 Explicación

Este proyecto estudia un sistema de colas con:

* **Llegadas Poisson** con tasa λ.
* **Servicio exponencial** con tasa μ.
* **Un solo servidor (M/M/1)**.
* **Capacidad máxima del sistema K**, por lo que los clientes que llegan cuando el sistema está lleno son bloqueados.

Se calcularon las métricas teóricas mediante el modelo matemático y se comprobaron mediante simulación en **Python**.

El código está implementado en un solo archivo (`mm1k_simulacion.py`) sin usar programación orientada a objetos.

## ⚙️ Requisitos

Antes de ejecutar el programa, debes tener instalado **Python 3** y el paquete **NumPy**.

Para instalar NumPy en tu entorno:

```bash
python3 -m venv venv
source venv/bin/activate
pip install numpy
```

## ▶️ Ejecución

Ejecuta el archivo principal:

```bash
python3 mm1k_simulacion.py
```

## 📊 Ejemplo de salida

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

## ✅ Conclusión

El modelo matemático y la simulación muestran valores muy cercanos, validando la correcta implementación del sistema **M/M/1/K** en Python.

---

👉 ¿Quieres que lo prepare en formato **`README.md` listo para que lo copies y pegues en tu repositorio**, o prefieres que lo exporte ya en un archivo `.md` descargable?

