import pandas as pd
import matplotlib.pyplot as plt

from curve import generate_curve

# Load assignment data
data = pd.read_csv("../data/xy_data.csv")

# Known solution (for verification)
theta = 30
M = 0.03
X = 55

curve_x, curve_y = generate_curve(theta, M, X)

plt.figure(figsize=(8, 8))

# Assignment points
plt.scatter(
    data["x"],
    data["y"],
    s=8,
    label="Assignment Data"
)

# Generated curve
plt.plot(
    curve_x,
    curve_y,
    color="red",
    linewidth=2,
    label="Generated Curve"
)

plt.axis("equal")
plt.grid(True)

plt.legend()

plt.show()