import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
import matplotlib.pyplot as plt

# 1) مدل دینامیکی: رشد لجستیک
# dX/dt = r * X * (1 - X / K)
def logistic_model(t, X, r, K):
    return r * X * (1 - X / K)

# 2) ساختن داده‌ی مصنوعی (شبیه داده‌ی آزمایشگاهی)
true_r = 0.6     # نرخ رشد واقعی
true_K = 1.2     # ظرفیت نهایی
X0 = [0.1]       # مقدار اولیه

t_eval = np.linspace(0, 10, 25)  # 25 نقطه در زمان
sol_true = solve_ivp(
    lambda t, x: logistic_model(t, x, true_r, true_K),
    [t_eval[0], t_eval[-1]],
    X0,
    t_eval=t_eval
)

# اضافه کردن نویز تا شبیه داده‌ی واقعی بشه
noise = 0.03 * np.random.randn(len(t_eval))
X_data = sol_true.y[0] + noise

# 3) تابعی برای شبیه‌سازی با پارامترهای دلخواه
def simulate_logistic(params, t, X0):
    r, K = params
    sol = solve_ivp(
        lambda t, x: logistic_model(t, x, r, K),
        [t[0], t[-1]],
        X0,
        t_eval=t
    )
    return sol.y[0]

# 4) تابع cost برای least squares
def residuals(params, t, X0, X_obs):
    X_sim = simulate_logistic(params, t, X0)
    return X_sim - X_obs

# 5) حدس اولیه برای پارامترها
initial_guess = [0.3, 1.0]  # r, K

result = least_squares(
    residuals,
    initial_guess,
    args=(t_eval, X0, X_data),
    bounds=([0.0, 0.1], [2.0, 5.0])
)

est_r, est_K = result.x
print(f"Estimated r = {est_r:.3f}")
print(f"Estimated K = {est_K:.3f}")

# 6) شبیه‌سازی دوباره با پارامترهای تخمینی
X_est = simulate_logistic([est_r, est_K], t_eval, X0)

# 7) رسم نتایج
plt.figure()
plt.scatter(t_eval, X_data, label="Measured data", marker="o")
plt.plot(t_eval, X_est, label="Fitted model", linewidth=2)
plt.plot(t_eval, sol_true.y[0], "--", label="True model (hidden)")
plt.xlabel("Time")
plt.ylabel("Biomass / Concentration")
plt.legend()
plt.title("Dynamic modeling of microbial growth")
plt.show()
