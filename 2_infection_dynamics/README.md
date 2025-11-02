# Infection Dynamics Model (Host–Pathogen)

This example models the interaction between:
- a bacterial population **B(t)**, and
- the host immune response **I(t)**.

The model includes:
- bacterial growth with a carrying capacity,
- immune-mediated killing of bacteria,
- activation and decay of the immune response.

**Equations:**

- dB/dt = rB · B · (1 - B/K) − k1 · I · B  
- dI/dt = rI · I · (B / (B + h)) − k2 · I

This type of model is common in computational biology and can be extended to pathogen–host systems in aquaculture.

**Run:**
```bash
pip install numpy scipy matplotlib
python infection_model.py
