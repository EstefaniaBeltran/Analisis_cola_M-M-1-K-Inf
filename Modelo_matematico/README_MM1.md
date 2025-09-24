
# Modelo Matemático del Sistema M/M/1

Este documento presenta el desarrollo paso a paso del modelo **M/M/1** en función de la tasa de llegada ($\lambda$) y la tasa de servicio ($\mu$).

---

## Paso 1: Definir parámetros fundamentales

- $\lambda$: tasa de llegada de usuarios.  
- $\mu$: tasa de servicio del sistema.  
- Factor de utilización:  

$$\rho = \frac{\lambda}{\mu}, \quad \rho < 1$$

El sistema es estable solo si $\rho < 1$.

---

## Paso 2: Número esperado de usuarios en el sistema (NS)

$$L = \frac{\rho}{1 - \rho} = \frac{\lambda}{\mu - \lambda}$$

---

## Paso 3: Tiempo esperado en el sistema (TS)

Aplicando la ley de Little:  

$$W = \frac{L}{\lambda} = \frac{1}{\mu - \lambda}$$

---

## Paso 4: Número esperado de usuarios en cola (NW)

$$L_q = L - \rho = \frac{\lambda}{\mu - \lambda} - \frac{\lambda}{\mu}$$

Simplificando:  

$$L_q = \frac{\lambda^2}{\mu(\mu - \lambda)}$$

---

## Paso 5: Tiempo esperado en cola (TW)

Nuevamente aplicando la ley de Little:  

$$W_q = \frac{L_q}{\lambda} = \frac{\lambda}{\mu(\mu - \lambda)}$$

---

# Resumen de Fórmulas

- Utilización:  
  $$\rho = \frac{\lambda}{\mu}$$

- Número esperado en el sistema:  
  $$L = \frac{\lambda}{\mu - \lambda}$$

- Número esperado en cola:  
  $$L_q = \frac{\lambda^2}{\mu(\mu - \lambda)}$$

- Tiempo medio en el sistema:  
  $$W = \frac{1}{\mu - \lambda}$$

- Tiempo medio en cola:  
  $$W_q = \frac{\lambda}{\mu(\mu - \lambda)}$$
