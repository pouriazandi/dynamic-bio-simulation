# Enzyme Kinetics (Dynamic model)

This folder contains a simple dynamic model of an enzyme-catalyzed reaction based on:
- E + S ⇄ ES → E + P

The model tracks:
- substrate (S),
- enzyme–substrate complex (ES),
- product (P)

and assumes a fixed total enzyme concentration.

**Run:**
```bash
pip install numpy scipy matplotlib
python enzyme_model.py
