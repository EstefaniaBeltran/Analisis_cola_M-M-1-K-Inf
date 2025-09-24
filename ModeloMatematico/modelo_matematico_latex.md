
# Modelo Matemático M/M/1/K/Infinita

El modelo matemático paso a paso de una cola M/M/1/K/Infinita.  

---

## 1) Definiciones y notación

- Llegadas: Poisson con tasa $\lambda$.  
- Servicio: Exponencial con tasa $\mu$.  
- Número de servidores: $1$.  
- Capacidad máxima del sistema: $K$.  
- Población fuente: Infinita.  
- Factor de utilización:  

```math
\rho = \frac{\lambda}{\mu}
```

---

## 2) Distribución estacionaria $P_n$

Para $0 \le n \le K$:

```math
\lambda P_n = \mu P_{n+1} \quad \Rightarrow \quad P_{n+1} = \rho P_n
```

De forma recursiva:

```math
P_n = P_0 \rho^n
```

**Normalización:**  

```math
\sum_{n=0}^K P_n = 1 \quad \Rightarrow \quad P_0 = \frac{1-\rho}{1-\rho^{K+1}}, \quad (\rho \neq 1)
```

Por tanto:

```math
P_n = \frac{1-\rho}{1-\rho^{K+1}} \rho^n, \quad 0 \le n \le K
```

**Caso especial $\rho=1$:**
```math
P_n = \frac{1}{K+1}, \quad 0 \le n \le K
```

---

## 3) Probabilidad de bloqueo y tasa efectiva

- Probabilidad de sistema lleno (bloqueo):  

```math
P_K = \frac{(1-\rho)\rho^K}{1-\rho^{K+1}}, \quad (\rho \neq 1)
```

- Tasa efectiva de llegadas:  

```math
\lambda_{\text{eff}} = \lambda(1 - P_K)
```

---

## 4) Número de usuarios en el sistema $NS$

```math
\sum_{n=0}^K n \rho^n = \frac{\rho (1 - (K+1)\rho^K + K\rho^{K+1})}{(1-\rho)^2}
```

Multiplicando por $P_0$:  

```math
NS = \frac{\rho(1-(K+1)\rho^K+K\rho^{K+1})}{(1-\rho)(1-\rho^{K+1})}, \quad (\rho \neq 1)
```

**Caso $\rho=1$:**
```math
NS = \frac{K}{2}
```

---

## 5) Número de usuarios en cola $Nw$

```math
Nw = NS - (1-P_0)
```

**Caso $\rho=1$:**
```math
Nw = \frac{K(K-1)}{2(K+1)}
```

---

## 6) Tiempos medios $W$ y $W_q$

```math
W = \frac{NS}{\lambda_{\text{eff}}}, \quad W_q = \frac{Nw}{\lambda_{\text{eff}}}
```

Relación alternativa:  

```math
W_q = W - \frac{1}{\mu}
```

**Caso $\rho=1$:**
```math
\lambda_{\text{eff}} = \lambda \frac{K}{K+1}
```
```math
W = \frac{K+1}{2\lambda}, \quad W_q = \frac{K+1}{2\lambda} - \frac{1}{\mu}
```

---

## 7) Resumen de fórmulas

**Para $\rho \neq 1$:**
```math
P_0 = \frac{1-\rho}{1-\rho^{K+1}}, \quad P_n = P_0 \rho^n, \quad P_K = P_0 \rho^K
```
```math
\lambda_{\text{eff}} = \lambda(1-P_K)
```
```math
NS = \frac{\rho(1-(K+1)\rho^K + K\rho^{K+1})}{(1-\rho)(1-\rho^{K+1})}
```
```math
Nw = NS - (1-P_0)
```
```math
W = \frac{NS}{\lambda_{\text{eff}}}, \quad W_q = W - \frac{1}{\mu}
```

**Caso $\rho=1$:**
```math
P_n = \frac{1}{K+1}, \quad P_K = \frac{1}{K+1}
```
```math
\lambda_{\text{eff}} = \lambda \frac{K}{K+1}
```
```math
L = \frac{K}{2}, \quad L_q = \frac{K(K-1)}{2(K+1)}
```
```math
W = \frac{K+1}{2\lambda}, \quad W_q = \frac{K+1}{2\lambda} - \frac{1}{\mu}
```

---

## 8) Notas finales

- Este modelo es válido para colas **M/M/1/K** con población infinita y capacidad máxima $K$.  
- Todas las fórmulas están listas para usarse en cálculos teóricos o implementaciones.  
