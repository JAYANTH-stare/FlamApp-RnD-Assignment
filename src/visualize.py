import pandas as pd
import matplotlib.pyplot as plt

from curve import generate_curve
from utils import load_parameters

# Load data
data = pd.read_csv("../data/xy_data.csv")

theta, M, X = load_parameters()

curve_x, curve_y = generate_curve(theta, M, X, num_points=3000)

plt.figure(figsize=(8, 8))

plt.scatter(
    data["x"],
    data["y"],
    s=6,
    alpha=0.7,
    label="Observed Data",
)

plt.plot(
    curve_x,
    curve_y,
    linewidth=2,
    label="Recovered Curve",
)

plt.title("Recovered Parametric Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid(True)
plt.legend()

plt.savefig("../outputs/comparison.png", dpi=300)

plt.show()