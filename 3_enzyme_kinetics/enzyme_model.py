import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# مدل ساده کینتیک آنزیمی بر پایه E + S <-> ES -> E + P

def enzyme_model(t, y, k1, k_1, k2, E_total):
    S, ES, P = y
    # آنزیم آزاد = آنزیم کل - آنزیم متصل
    E = E_total - ES
    dSdt = -k1 * E * S + k_1 * ES
    dESdt = k1 * E * S - (k_1 + k2) * ES
    dPdt = k2 * ES
    return [dSdt, dESdt, dPdt]

# پارامترها
k1 = 1.0     # ضریب اتصال
k_1 = 0.5    # ضریب جداشدن
k2 = 0.2     # ضریب تبدیل به محصول
E_total = 1.0  # کل آنزیم
params = (k1, k_1, k2, E_total)

# مقدار اولیه: سوبسترا داریم، محصول نداریم
S0 = 1.0
ES0 = 0.0
P0 = 0.0
y0 = [S0, ES0, P0]

t_eval = np.linspace(0, 20, 200)

sol = solve_ivp(
    enzyme_model,
    [t_eval[0], t_eval[-1]],
    y0,
    t_eval=t_eval,
    args=params
)

S = sol.y[0]
ES = sol.y[1]
P = sol.y[2]

plt.figure()
plt.plot(t_eval, S, label="Substrate (S)")
plt.plot(t_eval, P, label="Product (P)")
plt.plot(t_eval, ES, label="Complex (ES)")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("Enzyme kinetics (Michaelis–Menten style dynamics)")
plt.legend()
plt.tight_layout()
plt.show()
