import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution

from curve import generate_curve


# Load assignment data
data = pd.read_csv("../data/xy_data.csv")

actual_x = data["x"].values
actual_y = data["y"].values


def objective(params):
    """
    Objective function to minimize.

    params = [theta, M, X]
    """

    theta, M, X = params

    pred_x, pred_y = generate_curve(theta, M, X)

    error = np.abs(actual_x - pred_x) + np.abs(actual_y - pred_y)

    return np.mean(error)


bounds = [
    (0, 50),       # theta
    (-0.05, 0.05), # M
    (0, 100)       # X
]


result = differential_evolution(
    objective,
    bounds,
    seed=42,
    maxiter=100,
    polish=True
)


print("\nEstimated Parameters")
print("---------------------")
print(f"Theta : {result.x[0]:.6f} degrees")
print(f"M     : {result.x[1]:.6f}")
print(f"X     : {result.x[2]:.6f}")

print("\nFinal Error:", result.fun)