
# Modelo matemático Cola  M/M/1/k/Inf

**Objetivo:** presentar el desarrollo matemático detallado del modelo M/M/1 (capacidad infinita) en función de $\lambda$ (tasa de llegada) y $\mu$ (tasa de servicio).

---

## 1. Supuestos y notación

- Llegadas: proceso de Poisson con tasa $\lambda$.  
- Servicio: tiempos i.i.d. exponenciales con tasa $\mu$.  
- Un único servidor.  
- Definimos la utilización:
  $$\rho = \frac{\lambda}{\mu}.$$
  El sistema es estable si y solo si $\rho < 1$ (esto garantizará la convergencia de las sumas infinitas).

- Notación usada en la guía / tarea:
  - $P_n$: probabilidad de que el sistema tenga exactamente $n$ clientes (incluye el que está en servicio).  
  - $NS = L$: número medio de usuarios en el sistema.  
  - $NW = L_q$: número medio de usuarios en cola (esperando).  
  - $TS = W$: tiempo medio en el sistema (cola + servicio).  
  - $TW = W_q$: tiempo medio en cola.

---

## 2. Probabilidades de estado $P_n$ (ecuaciones de balance)

1. **Balance de flujo entre estados $n$ y $n+1$.**  
   En estado estacionario, la tasa media de transiciones hacia la derecha (llegadas) desde $n$ a $n+1$ debe igualar la tasa media de transiciones hacia la izquierda (servicios) desde $n+1$ a $n$. Es decir:
   $$\lambda P_n = \mu P_{n+1}.$$

2. **Obtener la relación recursiva.**
   De la ecuación anterior:
   $$P_{n+1} = \frac{\lambda}{\mu} P_n = \rho P_n.$$

3. **Resolución por recurrencia.**
   Aplicando la relación recursiva por inducción:
   $$P_n = P_0 \rho^n,\qquad n=0,1,2,\dots$$

4. **Normalización (cálculo de $P_0$).**  
   Como las $P_n$ deben sumar 1:
   $$\sum_{n=0}^{\infty} P_n = P_0 \sum_{n=0}^{\infty} \rho^n = P_0 \cdot \frac{1}{1-\rho} = 1\quad(\text{válido si }|\rho|<1).$$
   De donde:
   $$\boxed{P_0 = 1 - \rho}$$
   y, por tanto,
   $$\boxed{P_n = (1-\rho)\,\rho^n.}$$

---

## 3. Cálculo del número medio en el sistema $L = NS$

1. **Definición de la esperanza:**
   $$L = \mathbb{E}[N] = \sum_{n=0}^{\infty} n P_n = (1-\rho)\sum_{n=0}^{\infty} n \rho^n.$$

2. **Suma clave (demostración):**   
   Empezamos con la serie geométrica:
   $$S(x) = \sum_{n=0}^{\infty} x^n = \frac{1}{1-x},\qquad |x|<1.$$
   Derivando ambos lados respecto a $x$:
   $$S'(x) = \sum_{n=0}^{\infty} n x^{n-1} = \frac{1}{(1-x)^2}.$$
   Multiplicamos por $x$ para obtener
   $$\sum_{n=0}^{\infty} n x^n = \frac{x}{(1-x)^2}.$$

3. **Aplicación con $x=\rho$:**
   $$L = (1-\rho)\cdot\frac{\rho}{(1-\rho)^2} = \frac{\rho}{1-\rho}.$$

4. **Expresión en $\lambda$ y $\mu$:**
   Sustituyendo $\rho=\dfrac{\lambda}{\mu}$:
   \begin{align*}
   L &= \frac{\rho}{1-\rho} = \frac{\lambda/\mu}{1 - \lambda/\mu} 
       = \frac{\lambda/\mu}{(\mu-\lambda)/\mu} = \frac{\lambda}{\mu-\lambda}.
   \end{align*}

   $$\boxed{NS = L = \frac{\rho}{1-\rho} = \frac{\lambda}{\mu-\lambda}.}$$

---

## 4. Cálculo del número medio en cola $L_q = NW$

1. **Observación:** el servidor puede atender como máximo a 1 cliente simultáneo. El número esperado de clientes en servicio es la probabilidad de que el servidor esté ocupado. Dado que $P_0$ es la probabilidad de que no haya clientes, la probabilidad de que el servidor esté ocupado es:
   $$\Pr(\text{servidor ocupado}) = 1 - P_0 = 1 - (1-\rho) = \rho.$$

2. **Relación entre $L$ y $L_q$:**
   El total esperado $L$ se compone de clientes en cola ($L_q$) más los clientes en servicio (esperanza = $\rho$):
   $$L = L_q + \rho \quad\Rightarrow\quad L_q = L - \rho.$$

3. **Sustituir $L$:**
   \begin{align*}
   L_q &= \frac{\rho}{1-\rho} - \rho 
       = \rho\left(\frac{1}{1-\rho} - 1\right) 
       = \rho\left(\frac{1 - (1-\rho)}{1-\rho}\right)
       = \frac{\rho^2}{1-\rho}.
   \end{align*}

4. **En términos de $\lambda,\mu$:**
   \begin{align*}
   L_q &= \frac{\rho^2}{1-\rho} = \frac{(\lambda/\mu)^2}{1 - \lambda/\mu} 
         = \frac{\lambda^2/\mu^2}{(\mu-\lambda)/\mu} = \frac{\lambda^2}{\mu(\mu-\lambda)}.
   \end{align*}

   $$\boxed{NW = L_q = \frac{\rho^2}{1-\rho} = \frac{\lambda^2}{\mu(\mu-\lambda)}.}$$

---

## 5. Tiempo medio en el sistema $W = TS$ (Ley de Little)

1. **Ley de Little:** para el sistema en su conjunto se cumple
   $$L = \lambda W.$$

2. **Despejar $W$ y sustituir $L$:**
   $$W = \frac{L}{\lambda} = \frac{1}{\lambda}\cdot\frac{\lambda}{\mu-\lambda} = \frac{1}{\mu-\lambda}.$$

   $$\boxed{TS = W = \frac{1}{\mu-\lambda}.}$$

3. **Relación alternativa (verificación):**
   El tiempo total es tiempo en cola más tiempo de servicio medio:
   $$W = W_q + \frac{1}{\mu},$$
   que debe cumplirse si las demás fórmulas son correctas.

---

## 6. Tiempo medio en cola $W_q = TW$

1. **Little para la cola:** las llegadas (tasa $\lambda$) que contribuyen a la cola verifican
   $$L_q = \lambda W_q.$$

2. **Despejar $W_q$:**
   $$W_q = \frac{L_q}{\lambda}.$$

3. **Sustituyendo $L_q$:**
   $$W_q = \frac{1}{\lambda}\cdot\frac{\lambda^2}{\mu(\mu-\lambda)} = \frac{\lambda}{\mu(\mu-\lambda)}.$$

4. **Verificación con la relación servicio:** usando $W = W_q + 1/\mu$ se obtiene la misma expresión.

   $$\boxed{TW = W_q = \frac{\lambda}{\mu(\mu-\lambda)}.}$$

---

## 7. Resumen final — fórmulas listas (copiar y pegar)

Condición: $\rho = \dfrac{\lambda}{\mu} < 1$.

- Distribución de estados:
  $$P_n = (1-\rho)\rho^n,\qquad n=0,1,2,\dots$$

- Número medio en el sistema (NS):
  $$NS = L = \frac{\rho}{1-\rho} = \frac{\lambda}{\mu-\lambda}.$$

- Número medio en cola (NW):
  $$NW = L_q = \frac{\rho^2}{1-\rho} = \frac{\lambda^2}{\mu(\mu-\lambda)}.$$

- Tiempo medio en el sistema (TS):
  $$TS = W = \frac{1}{\mu-\lambda}.$$

- Tiempo medio en cola (TW):
  $$TW = W_q = \frac{\lambda}{\mu(\mu-\lambda)}.$$

---

## 8. Comentarios y comprobaciones rápidas

- **Condición de estabilidad:** siempre verifica que $\lambda < \mu$ antes de aplicar estas fórmulas. Si $\lambda \ge \mu$ el sistema no tiene estado estacionario (las sumas divergen).  
- **Chequeos numéricos:** para comprobar que no hay errores algebraicos, sustituye valores simples (ej.: $\lambda=2$, $\mu=3$) y comprueba que Little se cumple: $W \stackrel{?}{=} L/\lambda$ y $W_q \stackrel{?}{=} L_q/\lambda$.  
- **Notas:** las fórmulas se derivan suponiendo tiempos de servicio exponenciales e independientes, y llegadas Poisson; cambiar esas suposiciones requiere otro modelo (por ejemplo M/G/1).

---

## 9. Ejemplo numérico rápido (verificación)

Tomemos $\lambda = 2$, $\mu = 3$ (entonces $\rho = 2/3$):

- $L = \dfrac{\lambda}{\mu-\lambda} = \dfrac{2}{1} = 2.$  
- $L_q = \dfrac{\lambda^2}{\mu(\mu-\lambda)} = \dfrac{4}{3\cdot 1} = \tfrac{4}{3}\approx 1.333\ldots$  
- $W = \dfrac{1}{\mu-\lambda} = 1.$  
- $W_q = \dfrac{\lambda}{\mu(\mu-\lambda)} = \dfrac{2}{3\cdot 1} = \tfrac{2}{3}\approx 0.666\ldots$

Se verifica Little: $W = L/\lambda = 2/2 = 1$ y $W_q = L_q/\lambda = (4/3)/2 = 2/3$.

---

**Fin del desarrollo completo.**

Puedes copiar/pegar este archivo `README_MM1_full.md` directamente en el README de tu repositorio en GitHub; las ecuaciones escritas con `$$ ... $$` y `$ ... $` se renderizan correctamente en GitHub.

