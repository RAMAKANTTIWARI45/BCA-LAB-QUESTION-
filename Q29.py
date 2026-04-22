import pandas as pd

# Sample data (you can also read from CSV)
data = {
    'Name': ['Amit', 'Ravi', 'Sita', 'Geeta', 'Ram'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 40000, 60000, 45000, 70000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# -------------------------------
# 🔹 Filtering: Salary > 50000
# -------------------------------
filtered_data = df[df['Salary'] > 50000]

print("\nFiltered Data (Salary > 50000):")
print(filtered_data)

# -------------------------------
# 🔹 Grouping: Group by Department
# -------------------------------
grouped_data = df.groupby('Department')['Salary'].mean()

print("\nGrouped Data (Average Salary by Department):")
print(grouped_data)