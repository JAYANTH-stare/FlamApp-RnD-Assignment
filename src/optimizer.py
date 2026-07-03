import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution
from scipy.spatial import cKDTree
from curve import generate_curve


# Load assignment data
data = pd.read_csv("../data/xy_data.csv")

actual_x = data["x"].values
actual_y = data["y"].values


def objective(params):
    """
    Objective function using nearest-neighbour search.
    """

    theta, M, X = params

    pred_x, pred_y = generate_curve(
        theta,
        M,
        X,
        num_points=3000
    )

    predicted_points = np.column_stack((pred_x, pred_y))

    actual_points = np.column_stack((actual_x, actual_y))

    tree = cKDTree(predicted_points)

    distances, _ = tree.query(actual_points)

    return np.mean(distances)


bounds = [
    (0, 50),       # theta
    (-0.05, 0.05), # M
    (0, 100)       # X
]


result = differential_evolution(
    objective,
    bounds,
    strategy="best1bin",
    maxiter=250,
    popsize=20,
    tol=1e-7,
    mutation=(0.5, 1),
    recombination=0.7,
    seed=42,
    polish=True
)


theta = result.x[0]
M = result.x[1]
X = result.x[2]

print("=" * 40)
print("Recovered Parameters")
print("=" * 40)

print(f"Theta : {theta:.8f} degrees")
print(f"M     : {M:.8f}")
print(f"X     : {X:.8f}")

print("\nAverage Nearest-Point Error")

print(result.fun)