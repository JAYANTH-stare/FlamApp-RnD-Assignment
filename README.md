# FlamApp AI – Research & Development Assignment

![Python](https://img.shields.io/badge/Python-3.11-blue)
![SciPy](https://img.shields.io/badge/SciPy-Optimization-orange)
![NumPy](https://img.shields.io/badge/NumPy-Mathematics-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This repository contains my solution for the **FlamApp AI Research & Development Assignment**.

The objective of this assignment is to recover the unknown parameters of a nonlinear parametric curve from a given set of observed 2D points.

Unlike a straightforward mathematical implementation, this problem represents an **inverse parameter estimation** task where the original generating parameters are unknown and must be estimated by minimizing the geometric difference between the observed and reconstructed curves.

---

# Problem Statement

Given the following parametric equations

\[
x=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
\]

\[
y=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
\]

where

```
6 ≤ t ≤ 60
```

Unknown parameters

- θ (Rotation Angle)
- M (Exponential Growth Factor)
- X (Horizontal Translation)

The objective is to estimate these unknown variables using the provided dataset **xy_data.csv**.

---

# Optimization Workflow

```text
                    FlamApp AI R&D Assignment Workflow

                  +------------------------------+
                  |        xy_data.csv           |
                  |   (Observed Curve Points)    |
                  +--------------+---------------+
                                 |
                                 v
                  +------------------------------+
                  |       Load Dataset           |
                  |       (Pandas DataFrame)     |
                  +--------------+---------------+
                                 |
                                 v
                  +------------------------------+
                  | Implement Parametric Equation |
                  |      x(t), y(t) Model         |
                  +--------------+---------------+
                                 |
                                 v
                  +------------------------------+
                  | Generate Predicted Curve      |
                  | (Uniform Sampling of t)       |
                  +--------------+---------------+
                                 |
                                 v
                  +------------------------------+
                  | KD-Tree Nearest Neighbor      |
                  |  Match Observed ↔ Predicted   |
                  +--------------+---------------+
                                 |
                                 v
                  +------------------------------+
                  | Compute Objective Function    |
                  +--------------+---------------+
                                 |
                                 v
                  +------------------------------+
                  | Differential Evolution        |
                  | Parameter Optimization        |
                  +--------------+---------------+
                                 |
                                 v
                  +------------------------------+
                  | Recover θ, M and X            |
                  +--------------+---------------+
                                 |
                                 v
                  +------------------------------+
                  | Visualization & Evaluation    |
                  +------------------------------+
```

---

# Methodology

The complete solution consists of the following stages.

1. Load the observed dataset.
2. Implement the given mathematical model.
3. Uniformly sample the parameter **t** over the specified range.
4. Generate the predicted parametric curve.
5. Build a KD-Tree from the predicted points.
6. Match each observed point with its nearest predicted point.
7. Compute the average nearest-neighbour distance.
8. Minimize this objective using Differential Evolution.
9. Export the recovered parameters.
10. Validate the solution visually.

---

# Why Differential Evolution?

The optimization problem is nonlinear and contains three continuous unknown variables.

Differential Evolution was selected because

- It performs global optimization.
- It avoids becoming trapped in local minima.
- It does not require gradient information.
- It is robust for nonlinear objective functions.
- It performs well for bounded continuous search spaces.

---

# Why Was a KD-Tree Necessary?

During the initial implementation, the optimization compared corresponding indices of the observed and predicted points.

Although mathematically correct for ordered datasets, this approach produced incorrect parameter estimates because the provided dataset does **not preserve the original ordering of the parameter t**.

To overcome this limitation, the optimization was redesigned using a **KD-Tree nearest-neighbour search**.

The revised workflow is

1. Generate a dense predicted curve.
2. Construct a KD-Tree.
3. Find the nearest predicted point for every observed point.
4. Compute the average nearest-neighbour distance.
5. Minimize this distance using Differential Evolution.

This approach makes the optimization independent of the ordering of the dataset while remaining computationally efficient.

---

# Software Architecture

```text
FlamApp-RnD-Assignment

│
├── data
│     └── xy_data.csv
│
├── outputs
│     ├── comparison.png
│     ├── original_curve.png
│     ├── residual_histogram.png
│     ├── parameters.txt
│     └── results.json
│
├── src
│     ├── curve.py
│     ├── optimizer.py
│     ├── visualize.py
│     ├── residuals.py
│     ├── utils.py
│     └── main.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# Key Features

- Mathematical implementation of the given parametric equations.
- Differential Evolution based parameter estimation.
- KD-Tree nearest-neighbour curve matching.
- Automatic parameter export.
- Residual error visualization.
- Modular project structure.
- Reproducible optimization workflow.

---

# Final Results

Recovered Parameters

| Parameter | Estimated Value |
|-----------|----------------:|
| θ | **30.00003627°** |
| M | **0.03000046** |
| X | **55.00001394** |

Average nearest-neighbour error

```
0.0054797646
```

The recovered parameters closely reconstruct the original curve, demonstrating that the optimization successfully solved the inverse parameter estimation problem.

---

# Output

### Curve Comparison

![Comparison](outputs/comparison.png)

---

### Original Dataset

![Original Dataset](outputs/original_curve.png)

---

### Residual Error Distribution

![Residuals](outputs/residual_histogram.png)

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run optimization

```bash
python src/optimizer.py
```

Generate plots

```bash
python src/visualize.py
```

Residual analysis

```bash
python src/residuals.py
```

---

# Libraries Used

- NumPy
- Pandas
- SciPy
- Matplotlib

---

# Future Improvements

Potential future enhancements include

- Bayesian Optimization
- Particle Swarm Optimization
- Confidence interval estimation
- Multi-objective optimization
- GPU acceleration
- Interactive visualization dashboard

---

# Acknowledgements

This project was developed as part of the **FlamApp AI Research & Development Hiring Assignment**.

The implementation focuses on robust parameter estimation, clean software design, reproducibility, and clear documentation.

---

## References

1. R. Storn and K. Price, *Differential Evolution – A Simple and Efficient Heuristic for Global Optimization over Continuous Spaces*, Journal of Global Optimization, 1997.

2. SciPy Developers. *SciPy Optimization Documentation*. https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html

3. SciPy Developers. *scipy.spatial.cKDTree Documentation*. https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.cKDTree.html

4. NumPy Developers. *NumPy Documentation*. https://numpy.org/doc/

5. Matplotlib Developers. *Matplotlib Documentation*. https://matplotlib.org/stable/