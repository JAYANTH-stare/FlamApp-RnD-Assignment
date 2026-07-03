import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

from curve import generate_curve

data = pd.read_csv("../data/xy_data.csv")

actual = np.column_stack((data["x"], data["y"]))

pred_x, pred_y = generate_curve(
    30.00003627,
    0.03000046,
    55.00001394,
    num_points=3000,
)

predicted = np.column_stack((pred_x, pred_y))

tree = cKDTree(predicted)

distances, _ = tree.query(actual)

plt.figure(figsize=(8, 5))
plt.hist(distances, bins=30)
plt.title("Residual Error Distribution")
plt.xlabel("Nearest-Point Error")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("../outputs/residual_histogram.png", dpi=300)

plt.show()