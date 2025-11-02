# ----------------------------------------------------------
# Enzyme Kinetics Model (Michaelis–Menten type)
# Author: Pouria Alvarzandi
# Description:
#   Simulates a simple enzymatic reaction:
#   E + S ⇄ ES → E + P
#   Tracks the concentration of substrate (S),
#   enzyme-substrate complex (ES), and product (P) over time.
# ----------------------------------------------------------

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# (1) Define ODE system
def enzyme_model(t, y, k1, k_1, k2, E_total):
    S, ES, P = y
    E = E_total - ES  # free enzyme = total enzyme - bound enzyme

    # differential equations
    dSdt = -k1 * E * S + k_1 * ES
    dESdt = k1 * E * S - (k_1 + k2) * ES
    dPdt = k2 * ES

    return [dSdt, dESdt, dPdt]


# (2) Parameters
k1 = 1.0       # forward rate (binding)
k_1 = 0.5      # reverse rate (unbinding)
k2 = 0.2       # product formation rate
E_total = 1.0  # total enzyme

params = (k1, k_1, k2, E_total)

# (3) Initial conditions
S0 = 1.0   # initial substrate
ES0 = 0.0  # no complex yet
P0 = 0.0   # no product yet
y0 = [S0, ES0, P0]

t_eval = np.linspace(0, 20, 200)


# (4) Solve ODEs
sol = solve_ivp(
    enzyme_model,
    [t_eval[0], t_eval[-1]],
    y0,
    t_eval=t_eval,
    args=params
)

S, ES, P = sol.y  # extract results


# (5) Plot concentrations over time
plt.figure()
plt.plot(t_eval, S, label="Substrate (S)")
plt.plot(t_eval, ES, label="Complex (ES)")
plt.plot(t_eval, P, label="Product (P)")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("Enzyme Kinetics Simulation (Michaelis–Menten Dynamics)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
