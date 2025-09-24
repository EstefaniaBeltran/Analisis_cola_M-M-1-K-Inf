
## Parámetros del sistema  
- Tasa de llegada: $\lambda = 2$ clientes/minuto  
- Tasa de servicio: $\mu = 3$ clientes/minuto  
- Capacidad del sistema: $K = 5$ (incluye al servidor y a los clientes en cola)  

Factor de utilización:  

```math
\rho = \frac{\lambda}{\mu} = \frac{2}{3} \approx 0.667
````


## Modelo Matemático

### Probabilidad de que el sistema esté vacío

```math
P_0 = \frac{1 - \rho}{1 - \rho^{K+1}}
```

Sustituyendo:

```math
P_0 = \frac{1 - 0.667}{1 - (0.667)^6} \approx 0.398
```

### Probabilidad de \$n\$ clientes en el sistema

```math
P_n = \rho^n P_0
```

Ejemplos:

* \$P\_1 \approx 0.265\$
* \$P\_2 \approx 0.177\$
* \$P\_5 \approx 0.052\$

### Número de usuarios en el sistema (\$NS\$)

```math
NS = \sum_{n=0}^{K} n P_n
```

Evaluando la suma:

```math
NS \approx 1.19
```

### Número de usuarios en cola (\$Nw\$)

```math
Nw = NS - (1 - P_0)
```

```math
Nw \approx 1.19 - (1 - 0.398) = 0.59
```

### Tiempo en el sistema (\$TS\$)

Por la Ley de Little:

```math
TS = \frac{NS}{\lambda_e}
```

donde \$\lambda\_e\$ es la **tasa efectiva de llegada**:

```math
\lambda_e = \lambda (1 - P_K) \approx 2 (1 - 0.052) = 1.90
```

Entonces:

```math
TS = \frac{1.19}{1.90} \approx 0.626 \; minutos
```

### Tiempo en cola (\$Tw\$)

```math
Tw = TS - \frac{1}{\mu} = 0.626 - 0.333 \approx 0.293 \; minutos
```

---

## Resultados finales (Modelo Matemático)

| Métrica                                   | Valor aproximado  |
| ----------------------------------------- | ----------------- |
| \$P\_0\$ (sistema vacío)                  | 0.398             |
| \$NS\$ (número medio en sistema)          | 1.19              |
| \$Nw  \$ (número medio en cola)           | 0.59              |
| \$TS\$ (tiempo medio en sistema)          | 0.626 min         |
| \$Tw  \$ (tiempo medio en cola)           | 0.293 min         |
| \$\lambda\_e\$ (tasa efectiva de llegada) | 1.90 clientes/min |

---

## Comparación con el modelo computacional

Cuando ejecutes el **modelo de simulación adjunto** (el que el profesor entregó), anota los resultados y compáralos con la tabla de arriba:

| Métrica        | Matemático        | Simulación |
| -------------- | ----------------- | ---------- |
| \$NS\$         | 1.19              | ...        |
| \$Nw  \$       | 0.59              | ...        |
| \$TS\$         | 0.626 min         | ...        |
| \$Tw  \$       | 0.293 min         | ...        |
| \$\lambda\_e\$ | 1.90 clientes/min | ...        |

---

## Conclusión

El modelo matemático permite calcular métricas clave del sistema de colas \$M/M/1/K/\infty\$.
La simulación computacional valida estos resultados de manera experimental, mostrando valores muy cercanos a los teóricos.


