# Variable assignment
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

# Method 1: Swapping using a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping using temporary variable:")
print("a =", a)
print("b =", b)


# Re-assign values again for next method
a = 10
b = 20

# Method 2: Swapping without using temporary variable
a=a+b
b = a-b
a=a-b

print("\nAfter swapping without temporary variable:")
print("a =", a)
print("b =", b)