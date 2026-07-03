import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("../data/xy_data.csv")

# Plot
plt.figure(figsize=(8, 8))
plt.scatter(data["x"], data["y"], s=10)

plt.title("Provided Curve Data")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)
plt.axis("equal")

plt.savefig("../outputs/original_curve.png", dpi=300)

plt.show()