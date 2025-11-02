# Infection Dynamics (Bacteria vs Immune Response)

This model simulates an infection process with two variables:
- **B(t)**: bacteria population  
- **I(t)**: immune response intensity  

The bacteria try to grow, while the immune system suppresses them.  
Over time, the infection stabilizes as both sides reach equilibrium.

## 📘 Model
**Equations:**
```
dB/dt = rB * B * (1 - B / K) - k1 * I * B
dI/dt = rI * I * (B / (B + h)) - k2 * I
```

## ⚙️ Implementation
- Solved numerically using `scipy.integrate.solve_ivp`
- Realistic parameters to show infection control behavior

## 📊 Typical Behavior
- Bacteria increase rapidly at first  
- Immune response activates later and reduces bacteria  
- Finally, both populations reach steady state  

## ▶️ How to Run
```bash
pip install numpy scipy matplotlib
python infection_model.py
```