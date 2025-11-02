import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# مدل عفونت: باکتری (B) و سلول ایمنی (I)
def infection_model(t, y, rB, K, k1, rI, h, k2):
    B, I = y
    dBdt = rB * B * (1 - B / K) - k1 * I * B
    dIdt = rI * I * (B / (B + h)) - k2 * I
    return [dBdt, dIdt]

# پارامترها
rB = 0.8   # نرخ رشد باکتری
K = 5.0    # ظرفیت نهایی باکتری
k1 = 0.2   # قدرت خنثی‌سازی ایمنی
rI = 0.5   # نرخ فعال شدن ایمنی
h = 0.1    # آستانه تحریک
k2 = 0.1   # مرگ طبیعی سلول ایمنی

params = (rB, K, k1, rI, h, k2)

# زمان شبیه‌سازی
t_eval = np.linspace(0, 30, 200)

# مقدار اولیه: کمی باکتری، کمی ایمنی
y0 = [0.1, 0.05]

# حل معادلات
sol = solve_ivp(
    infection_model,
    [t_eval[0], t_eval[-1]],
    y0,
    t_eval=t_eval,
    args=params
)

B = sol.y[0]
I = sol.y[1]

# رسم
plt.figure()
plt.plot(t_eval, B, label="Bacteria (B)")
plt.plot(t_eval, I, label="Immune cells (I)")
plt.xlabel("Time")
plt.ylabel("Concentration / Count")
plt.title("Infection dynamics: bacteria vs immune response")
plt.legend()
plt.tight_layout()
plt.show()
