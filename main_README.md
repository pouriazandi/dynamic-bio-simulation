# Dynamic Modeling of Biological Systems (Python)

This repository contains three small examples of ODE-based (dynamic) models implemented in Python.

## 📁 Contents
1. **1_logistic_growth/** – logistic growth of a population (with parameter estimation)
2. **2_infection_dynamics/** – host–pathogen interaction (infection dynamics)
3. **3_enzyme_kinetics/** – enzyme reaction kinetics (E + S <-> ES -> E + P)

All examples use:
- Python 3.x  
- NumPy  
- SciPy (`solve_ivp`)  
- Matplotlib  

## ▶️ How to Run
```bash
pip install numpy scipy matplotlib
python <script_name>.py
```

Each folder includes its own README file with model details and equations.
