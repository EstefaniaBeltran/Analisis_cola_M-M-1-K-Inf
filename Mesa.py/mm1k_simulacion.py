import random
import numpy as np

# ----------------------------
# Parámetros del sistema
# ----------------------------
LAMBDA = 2.0     # tasa de llegada (clientes/min)
MU = 3.0         # tasa de servicio (clientes/min)
K = 5            # capacidad máxima del sistema
SIM_TIME = 10000 # tiempo total de simulación

# ----------------------------
# Variables del sistema
# ----------------------------
clock = 0
num_in_system = 0
blocked = 0
total_clients = 0
departures = []
queue = []
server_busy = False

# ----------------------------
# Simulación paso a paso
# ----------------------------
for t in range(SIM_TIME):
    # Llegada (Poisson aproximado)
    if random.random() < LAMBDA / (LAMBDA + MU):
        if num_in_system < K:
            total_clients += 1
            arrival_time = t
            queue.append(arrival_time)
            num_in_system += 1
        else:
            blocked += 1

    # Servicio (exponencial con tasa mu)
    if server_busy:
        if random.random() < MU / (LAMBDA + MU):
            arrival_time = queue.pop(0)
            departure_time = t
            departures.append(departure_time - arrival_time)
            num_in_system -= 1
            server_busy = False
    if not server_busy and len(queue) > 0:
        server_busy = True

# ----------------------------
# Cálculo de métricas
# ----------------------------
if departures:
    TS = np.mean(departures)
    Tw = TS - 1/MU
    NS = LAMBDA * (1 - blocked/total_clients) * TS
    Nw = NS - (1 - blocked/total_clients)
    lambda_e = LAMBDA * (1 - blocked/total_clients)
else:
    TS, Tw, NS, Nw, lambda_e = 0, 0, 0, 0, 0

# ----------------------------
# Resultados
# ----------------------------
print("Resultados simulación (M/M/1/K)")
print(f"NS (número medio en sistema): {NS:.4f}")
print(f"Nw (número medio en cola):    {Nw:.4f}")
print(f"TS (tiempo medio en sistema): {TS:.4f}")
print(f"Tw (tiempo medio en cola):    {Tw:.4f}")
print(f"λe (tasa efectiva de llegada): {lambda_e:.4f}")
print(f"Clientes bloqueados: {blocked}")
