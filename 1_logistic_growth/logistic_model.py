# ----------------------------------------------------------
# Logistic Growth Model
# Author: Pouria Alvarzandi
# Description:
#   This script simulates microbial/cell growth using a logistic model.
#   It generates synthetic data, fits parameters (r, K) using least squares,
#   and plots the results.
# ----------------------------------------------------------

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
import matplotlib.pyplot as plt


# (1) Define the logistic model
# dX/dt = r * X * (1 - X / K)
def logistic_model(t, X, r, K):
    return r * X * (1 - X / K)


# (2) Generate synthetic "experimental" data
true_r = 0.6      # true growth rate
true_K = 1.2      # true carrying capacity
X0 = [0.1]        # initial concentration

# simulate the true system
t_eval = np.linspace(0, 10, 25)
sol_true = solve_ivp(
    lambda t, x: logistic_model(t, x, true_r, true_K),
    [t_eval[0], t_eval[-1]],
    X0,
    t_eval=t_eval
)

# add small random noise to make it look experimental
noise = 0.03 * np.random.randn(len(t_eval))
X_data = sol_true.y[0] + noise


# (3) Helper function to simulate model for given parameters
def simulate_logistic(params, t, X0):
    r, K = params
    sol = solve_ivp(
        lambda t, x: logistic_model(t, x, r, K),
        [t[0], t[-1]],
        X0,
        t_eval=t
    )
    return sol.y[0]


# (4) Define residuals for least-squares fitting
def residuals(params, t, X0, X_obs):
    X_sim = simulate_logistic(params, t, X0)
    return X_sim - X_obs


# (5) Parameter estimation using least squares
initial_guess = [0.3, 1.0]
result = least_squares(
    residuals,
    initial_guess,
    args=(t_eval, X0, X_data),
    bounds=([0.0, 0.1], [2.0, 5.0])
)

est_r, est_K = result.x
print(f"Estimated r = {est_r:.3f}")
print(f"Estimated K = {est_K:.3f}")


# (6) Simulate model with estimated parameters
X_est = simulate_logistic([est_r, est_K], t_eval, X0)


# (7) Plot results
plt.figure()
plt.scatter(t_eval, X_data, label="Measured data", marker="o")
plt.plot(t_eval, X_est, label="Fitted model", linewidth=2)
plt.plot(t_eval, sol_true.y[0], "--", label="True model (hidden)")
plt.xlabel("Time")
plt.ylabel("Biomass / Concentration")
plt.legend()
plt.title("Dynamic modeling of microbial growth (Logistic Model)")
plt.show()
