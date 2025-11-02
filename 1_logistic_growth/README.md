# 🧠 Logistic Growth Model

This example demonstrates a simple **dynamic model of microbial growth**, following the classical *logistic equation*.

---

## 📘 Overview
The model describes how a population grows rapidly at first and then slows down as it reaches a **carrying capacity (K)** due to limited resources.

\[
\frac{dX}{dt} = r \cdot X \cdot \left(1 - \frac{X}{K}\right)
\]

Where:  
- **X** = population or biomass  
- **r** = growth rate  
- **K** = carrying capacity  

---

## ⚙️ Implementation
- Synthetic experimental data are generated with small random noise.  
- Model parameters (**r**, **K**) are estimated using the **least-squares optimization** method (`scipy.optimize.least_squares`).  
- The fitted model is compared against the original “true” model to evaluate accuracy.

---

## 📊 Example Output
When executed, the script prints:

