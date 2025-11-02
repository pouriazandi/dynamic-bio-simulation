
---

## 🦠 **2️⃣  `2_infection_dynamics/README.md`**

```markdown
# 🦠 Infection Dynamics (Host–Pathogen Model)

This model simulates the **interaction between bacteria (B)** and the **host immune response (I)** over time — a simplified version of what happens during infection in living organisms.

---

## 📘 Concept
The system is described by two differential equations:

\[
\frac{dB}{dt} = r_B B \left(1 - \frac{B}{K}\right) - k_1 I B
\]

\[
\frac{dI}{dt} = r_I I \left(\frac{B}{B + h}\right) - k_2 I
\]

Where:
- **B(t)** → bacterial population  
- **I(t)** → immune cell activity  
- **rB, rI** → growth and activation rates  
- **k₁, k₂** → killing and decay rates  
- **K, h** → saturation and activation constants  

---

## ⚙️ Implementation
- Solved numerically using `scipy.integrate.solve_ivp`.  
- Parameters chosen to produce realistic infection dynamics.  
- Output shows how the immune response first rises, then controls the infection.

---

## 📊 Typical Behavior
- Bacteria initially increase rapidly.  
- Immune response activates with a delay.  
- Eventually, the system reaches equilibrium (infection controlled).

---

## ▶️ How to Run
```bash
pip install numpy scipy matplotlib
python infection_model.py
