# 🧠 Dynamic Modeling of Biological Growth (Python)

This project demonstrates how to model and simulate a simple **biological growth system** using **ordinary differential equations (ODEs)** and **parameter estimation** techniques in Python.  
It is designed as a compact example of how AI, data-driven modeling, and computational biology can be integrated — inspired by the type of research conducted at the **Computational Biology Group (MBG-CSIC, Pontevedra)**.

---

## 🚀 Overview
The project simulates microbial (or cellular) growth following a **logistic model**:

\[
\frac{dX}{dt} = r \cdot X \cdot \left(1 - \frac{X}{K}\right)
\]

where:
- **X** = biomass or cell concentration  
- **r** = growth rate  
- **K** = carrying capacity  

The model is used to:
1. Generate synthetic “experimental” data with added noise  
2. Estimate the model parameters (**r**, **K**) using least-squares optimization  
3. Compare simulated and fitted results visually  

---

## 🧩 Workflow

- **Step 1:** Define the ODE system (logistic growth)  
- **Step 2:** Generate synthetic data with small random noise  
- **Step 3:** Estimate parameters by minimizing residuals  
- **Step 4:** Plot results for comparison  

---

## 🧠 Why this project
This small prototype shows:
- Understanding of **dynamic systems** and **simulation**  
- Ability to implement **numerical methods** (ODE solving + optimization)  
- Familiarity with **Python scientific libraries** (NumPy, SciPy, Matplotlib)  
- Potential to apply these tools in **computational biology** and **AI-based modeling**

It was developed as part of my preparation for applying to the **Contract ref#CB1 – Dynamic Simulation in Biological Systems (MBG-CSIC)** position.

---

## ⚙️ Requirements
To run the code, install dependencies:

```bash
pip install numpy scipy matplotlib