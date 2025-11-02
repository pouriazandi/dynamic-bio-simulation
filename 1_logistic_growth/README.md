# Logistic Growth Model

This example shows a basic dynamic model describing how a population (or biomass) grows over time until it reaches a limit due to resource constraints.

## 📘 Model
**Equation:**
```
dX/dt = r * X * (1 - X / K)
```

- `X`: population / biomass  
- `r`: growth rate  
- `K`: carrying capacity  

The script:
1. Simulates a "true" logistic model.  
2. Adds noise to create synthetic experimental data.  
3. Estimates parameters (`r`, `K`) from data using least-squares optimization.  

## 📊 Output
When you run the script, it prints estimated parameters like:
```
Estimated r = 0.598
Estimated K = 1.205
```

and displays a plot comparing:
- Measured (noisy) data  
- Fitted model  
- True model  

## ▶️ How to Run
```bash
pip install numpy scipy matplotlib
python logistic_model.py
```