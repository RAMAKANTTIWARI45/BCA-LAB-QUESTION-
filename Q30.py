import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# Create subplots (2 graphs in one window)
plt.figure(figsize=(8,6))

# Line graph
plt.subplot(2,1,1)
plt.plot(x, y, marker='o')
plt.title("Line Graph")

# Bar graph
plt.subplot(2,1,2)
plt.bar(categories, values)
plt.title("Bar Graph")

plt.tight_layout()
plt.show()