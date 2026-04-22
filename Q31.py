import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data
df = pd.read_csv("sales_data.csv")

print("----- Raw Data -----")
print(df)

# Step 2: Data Cleaning
df['Sales'].fillna(df['Sales'].mean(), inplace=True)
df['Profit'].fillna(df['Profit'].mean(), inplace=True)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Add New Column using NumPy
df['Profit_Percentage'] = np.where(df['Sales'] > 0,
                                   (df['Profit'] / df['Sales']) * 100,
                                   0)

# Step 4: Basic Analysis
print("\n----- Statistical Summary -----")
print(df.describe())

print("\nTotal Sales:", np.sum(df['Sales']))
print("Average Profit:", np.mean(df['Profit']))

# Step 5: Grouping (Region-wise)
region_data = df.groupby('Region').sum(numeric_only=True)

print("\n----- Region-wise Data -----")
print(region_data)

# Step 6: Visualization

# 1. Line Plot (Sales over time)
plt.figure()
plt.plot(df['Date'], df['Sales'], marker='o')
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()

# 2. Bar Plot (Profit by Region)
plt.figure()
region_data['Profit'].plot(kind='bar')
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")

# 3. Pie Chart (Sales Distribution)
plt.figure()
region_data['Sales'].plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution by Region")

# Step 7: Insights
max_sale_day = df.loc[df['Sales'].idxmax()]
print("\nHighest Sales Day:")
print(max_sale_day)

plt.show()
