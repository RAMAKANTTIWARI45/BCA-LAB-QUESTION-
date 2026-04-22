# Tuple operations and immutability demonstration

# Creating a tuple
t = (10, 20, 30, 40, 50)

print("Original Tuple:", t)

# Tuple operations
print("First element:", t[0])
print("Last element:", t[-1])
print("Sliced Tuple (1 to 3):", t[1:4])
print("Length of tuple:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# Demonstrating immutability
try:
    t[1] = 25   # This will cause an error
except TypeError:
    print("\nTuples are immutable! Cannot change elements.")

