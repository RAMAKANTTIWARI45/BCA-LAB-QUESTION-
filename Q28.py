import pandas as pd

# CSV file read karna
df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nShape of dataset:")
print(df.shape)