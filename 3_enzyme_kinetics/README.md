# Enzyme Kinetics (Michaelis–Menten Model)

This example simulates a simple enzymatic reaction over time using ordinary differential equations (ODEs).

## 📘 Reaction Scheme
```
E + S <-> ES -> E + P
```

Where:
- `E`: enzyme  
- `S`: substrate  
- `ES`: enzyme–substrate complex  
- `P`: product  

## ⚙️ Model Equations
```
dS/dt  = -k1 * E * S + k_1 * ES
dES/dt =  k1 * E * S - (k_1 + k2) * ES
dP/dt  =  k2 * ES
```

## 📊 Behavior
- Substrate (S) decreases  
- Complex (ES) increases, then decreases  
- Product (P) steadily increases  

## ▶️ How to Run
```bash
pip install numpy scipy matplotlib
python enzyme_model.py
```