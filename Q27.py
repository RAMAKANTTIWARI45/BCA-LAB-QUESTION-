import numpy as np

# 1. Array Creation
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

# 2. Indexing
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice (1 to 3):", arr[1:4])

# 3. 2D Array Creation
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# 4. Indexing in 2D array
print("Element at row 1, col 2:", arr2[1][2])

# 5. Arithmetic Operations
print("\nAddition:", arr + 5)
print("Multiplication:", arr * 2)
print("Square:", arr ** 2)

# 6. Array to Array Operations
arr3 = np.array([1, 1, 1, 1, 1])
print("\nArray Addition:", arr + arr3)