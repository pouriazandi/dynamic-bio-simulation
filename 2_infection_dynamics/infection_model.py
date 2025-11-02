# ----------------------------------------------------------
# Infection Dynamics Model (Host–Pathogen)
# Author: Pouria Alvarzandi
# Description:
#   This model simulates the interaction between bacteria (B)
#   and the host immune response (I).
#   It demonstrates dynamic behavior such as growth, inhibition,
#   and equilibrium between pathogen and immune cells.
# ----------------------------------------------------------

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# (1) Define the differential equations
def infection_model(t, y, rB, K, k1, rI, h, k2):
    B, I = y  # Bacteria and Immune cells
    dBdt = rB * B * (1 - B / K) - k1 * I * B  # bacteria growth + immune killing
    dIdt = rI * I * (B / (B + h)) - k2 * I    # immune activation + natural death
    return [dBdt, dIdt]


# (2) Define parameters
rB = 0.8   # bacterial growth rate
K = 5.0    # carrying capacity
k1 = 0.2   # immune killing rate
rI = 0.5   # immune activation rate
h = 0.1    # activation threshold
k2 = 0.1   # immune decay rate
params = (rB, K, k1, rI, h, k2)

# (3) Initial conditions
y0 = [0.1, 0.05]  # small initial infection and small immune response
t_eval = np.linspace(0, 30, 200)  # time points


# (4) Solve system using scipy's ODE solver
sol = solve_ivp(
    infection_model,
    [t_eval[0], t_eval[-1]],
    y0,
    t_eval=t_eval,
    args=params
)

B, I = sol.y  # extract bacteria and immune cell values


# (5) Plot results
plt.figure()
plt.plot(t_eval, B, label="Bacteria (B)", linewidth=2)
plt.plot(t_eval, I, label="Immune cells (I)", linewidth=2)
plt.xlabel("Time")
plt.ylabel("Concentration / Count")
plt.title("Infection Dynamics: Bacteria vs Immune Response")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
