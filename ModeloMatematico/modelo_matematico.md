
# Modelo Matemático M/M/1/K (Fuente Infinita)

Este documento presenta el **modelo matemático paso a paso** de una cola M/M/1/K con población fuente infinita.  

---

## 1) Definiciones y notación

- Llegadas: **Poisson** con tasa \(\lambda\).  
- Servicio: **Exponencial** con tasa \(\mu\).  
- Número de servidores: \(1\).  
- Capacidad máxima del sistema (incluye el servidor): \(K\).  
- Población fuente: Infinita.  
- Factor de utilización:  
\[\rho = \frac{\lambda}{\mu}.\]

---

## 2) Distribución estacionaria \(P_n\)

Para \(0 \le n \le K\):

\[\lambda P_n = \mu P_{n+1} \quad \Rightarrow \quad P_{n+1} = \rho P_n.\]

De forma recursiva:

\[P_n = P_0 \rho^n.\]

**Normalización:**  

\[\sum_{n=0}^K P_n = 1 \quad \Rightarrow \quad P_0 = \frac{1-\rho}{1-\rho^{K+1}}, \quad (\rho \neq 1).\]

Por tanto:

\[\boxed{P_n = \frac{1-\rho}{1-\rho^{K+1}} \rho^n, \quad 0 \le n \le K.}\]

**Caso especial \(\rho=1\):**

\[\boxed{P_n = \frac{1}{K+1}, \quad 0 \le n \le K.}\]

---

## 3) Probabilidad de bloqueo y tasa efectiva

- Probabilidad de sistema lleno (bloqueo):  

\[\boxed{P_K = \frac{(1-\rho)\rho^K}{1-\rho^{K+1}}, \quad (\rho \neq 1).}\]

- Tasa efectiva de llegadas:  

\[\boxed{\lambda_{\text{eff}} = \lambda(1 - P_K).}\]

---

## 4) Número medio en el sistema \(L\)

Se tiene:  

\[\sum_{n=0}^K n \rho^n = \frac{\rho \left(1 - (K+1)\rho^K + K\rho^{K+1}\right)}{(1-\rho)^2}.\]

Multiplicando por \(P_0\):  

\[\boxed{L = \frac{\rho\left(1-(K+1)\rho^K+K\rho^{K+1}\right)}{(1-\rho)(1-\rho^{K+1})}, \quad (\rho \neq 1).}\]

**Caso \(\rho=1\):**  

\[\boxed{L = \frac{K}{2}.}\]

---

## 5) Número medio en cola \(L_q\)

El número medio en cola se obtiene restando el servidor:  

\[\boxed{L_q = L - (1-P_0).}\]

**Caso \(\rho=1\):**  

\[\boxed{L_q = \frac{K(K-1)}{2(K+1)}.}\]

---

## 6) Tiempos medios \(W\) y \(W_q\)

Usando la ley de Little con la tasa efectiva:  

\[\boxed{W = \frac{L}{\lambda_{\text{eff}}}, \quad W_q = \frac{L_q}{\lambda_{\text{eff}}}.}\]

Relación alternativa:  

\[\boxed{W_q = W - \frac{1}{\mu}.}\]

**Caso \(\rho=1\):**  

\[\lambda_{\text{eff}} = \lambda \frac{K}{K+1},\]  
\[\boxed{W = \frac{K+1}{2\lambda}}, \quad \boxed{W_q = \frac{K+1}{2\lambda} - \frac{1}{\mu}}.\]

---

## 7) Resumen de fórmulas

**Para \(\rho \neq 1\):**  

\[\begin{aligned}
P_0 &= \frac{1-\rho}{1-\rho^{K+1}}, & P_n &= P_0 \rho^n, & P_K &= P_0 \rho^K, \\
\lambda_{\text{eff}} &= \lambda(1-P_K), \\
L &= \frac{\rho\left(1-(K+1)\rho^K + K\rho^{K+1}\right)}{(1-\rho)(1-\rho^{K+1})}, \\
L_q &= L - (1-P_0), \\
W &= \frac{L}{\lambda_{\text{eff}}}, & W_q &= W - \frac{1}{\mu}.
\end{aligned}\]

**Caso \(\rho=1\):**  

\[\begin{aligned}
P_n &= \frac{1}{K+1}, & P_K &= \frac{1}{K+1}, \\
\lambda_{\text{eff}} &= \lambda \frac{K}{K+1}, \\
L &= \frac{K}{2}, & L_q &= \frac{K(K-1)}{2(K+1)}, \\
W &= \frac{K+1}{2\lambda}, & W_q &= \frac{K+1}{2\lambda} - \frac{1}{\mu}.
\end{aligned}\]

---

## 8) Notas finales

- Este modelo es válido para colas **M/M/1/K** con población infinita y capacidad máxima \(K\).  
- Todas las fórmulas están listas para usarse en cálculos teóricos o implementaciones.  
