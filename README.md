# Analisis cola M/M/1/K/Inf
Perfecto — te lo dejo todo listo. Incluyo:

1. El **README final** (con sección de comparación).
2. Una **tabla de ejemplo** con los valores matemáticos que ya calculaste y una columna de *simulación de ejemplo* (usé los números que tenías de NetLogo como placeholder).
3. Un **script corto en Python (sin POO)** que calcula automáticamente el **error %** y muestra la tabla — así, cuando ejecutes tu simulación en Python sólo pegas esos resultados y el script hace la comparación por ti.

---

# README (actualizado)

## 📊 Simulación del sistema de colas M/M/1/K

### 🎯 Objetivos

* Implementar y analizar el sistema de colas $M/M/1/K$.
* Calcular métricamente $NS, Nw, TS, Tw, \lambda_e$.
* Validar los resultados del modelo matemático mediante simulación computacional en Python.
* Comparar errores relativos entre teoría y simulación.

### 📝 Descripción breve

Se presenta el modelo teórico y una implementación en Python (simulación discreta) que respeta la capacidad máxima $K$. Las métricas analizadas son:

* $NS$: número medio de clientes en el sistema.
* $Nw$: número medio en cola.
* $TS$: tiempo medio en el sistema.
* $Tw$: tiempo medio de espera en cola.
* $\lambda_e$: tasa efectiva de llegada.

### ⚙️ Requisitos

* **Python 3.8+**
* **NumPy** (recomendado) — instalar vía `sudo apt install python3-numpy -y` o usando un entorno virtual:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install numpy
  ```

### ▶️ Cómo ejecutar

1. Guarda y ejecuta tu script de simulación (por ejemplo `mm1k_simulacion.py`):

   ```bash
   python3 mm1k_simulacion.py
   ```
2. Anota los valores que imprima (NS, Nw, TS, Tw, λe).
3. Usa el script de comparación (más abajo) para obtener la tabla con los errores porcentuales automáticamente.

---

## 📈 Comparación: Matemático vs Simulación

> **Valores teóricos** (ya calculados):
>
> * $P_0 \approx 0.398$
> * $NS \approx 1.19$
> * $Nw \approx 0.59$
> * $TS \approx 0.626\ \text{min}$
> * $Tw \approx 0.293\ \text{min}$
> * $\lambda_e \approx 1.90\ \text{clientes/min}$

### Tabla (ejemplo con valores de simulación *placeholder*)

| Métrica           | Matemático | Simulación (ejemplo) | Error (%) |
| ----------------- | ---------: | -------------------: | --------: |
| NS                |       1.19 |                 1.24 |     4.20% |
| Nw                |       0.59 |                 0.65 |    10.17% |
| TS (min)          |      0.626 |                0.648 |     3.51% |
| Tw (min)          |      0.293 |                0.323 |    10.24% |
| λe (clientes/min) |       1.90 |                 1.91 |     0.53% |

> **Nota:** Los valores en “Simulación (ejemplo)” son los que tenías en tu README anterior (simulación en NetLogo). Cuando ejecutes la simulación en Python reemplaza esa columna por tus resultados reales y recalcula errores (puedes usar el script que viene abajo).

---

## ✅ Conclusión

La simulación valida el modelo matemático cuando las discrepancias permanecen en rangos pequeños (aquí < 10% en tu ejemplo). Las diferencias se explican por la variabilidad estocástica y por la duración finita de la simulación; aumentar `SIM_TIME` reduce la varianza de las estimaciones.

---

# Script auxiliar para comparar (sin POO — pega y ejecuta)

Guarda esto como `comparar_resultados.py`. Edita la sección `simulacion` con los valores que imprima tu `mm1k_simulacion.py` y luego ejecuta `python3 comparar_resultados.py`.

```python
# comparar_resultados.py
# Script simple (sin POO) para comparar resultados teóricos y de simulación
# Rellena la dict 'simulacion' con los resultados que obtengas de tu script.

import math

# Valores teóricos (los que calculaste)
teorico = {
    "NS": 1.19,
    "Nw": 0.59,
    "TS": 0.626,
    "Tw": 0.293,
    "lambda_e": 1.90
}

# --- EDITA ESTA PARTE con los resultados de TU simulación en Python ---
simulacion = {
    "NS": 1.24,        # <- reemplaza por el NS que obtuviste
    "Nw": 0.65,        # <- reemplaza por el Nw que obtuviste
    "TS": 0.648,       # <- reemplaza por el TS que obtuviste
    "Tw": 0.323,       # <- reemplaza por el Tw que obtuviste
    "lambda_e": 1.91   # <- reemplaza por lambda_e de la simulación
}
# ---------------------------------------------------------------------

def error_percent(real, approx):
    if real == 0:
        return float('nan')
    return abs((approx - real) / real) * 100.0

# Construir y mostrar tabla
headers = ["Métrica", "Matemático", "Simulación", "Error (%)"]
rows = []
for key in ["NS", "Nw", "TS", "Tw", "lambda_e"]:
    t = teorico[key]
    s = simulacion.get(key, float('nan'))
    e = error_percent(t, s)
    rows.append((key, t, s, e))

# Imprimir tabla formateada
print("{:<12} {:>12} {:>14} {:>12}".format(*headers))
for r in rows:
    key, t, s, e = r
    if math.isnan(e):
        e_str = "N/A"
    else:
        e_str = f"{e:.2f}%"
    print("{:<12} {:>12.4f} {:>14.4f} {:>12}".format(key, t, s, e_str))
```

---

Si quieres, yo puedo:

* Ejecutar el cálculo de la tabla por ti si me pegas los resultados que imprima `mm1k_simulacion.py`.
* O bien, incorporar la tabla resultante directamente al README y devolvértelo listo para entregar.

¿Qué prefieres: **me pegas los resultados** y yo te devuelvo el README final con la tabla ya completada, o **quieres que lo hagas tú** con el script y luego me muestres la salida?

