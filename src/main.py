import pandas as pd

# Load dataset
data = pd.read_csv("../data/xy_data.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

print("\nMissing Values:")
print(data.isnull().sum())