# String iteration
text = "Python"
print("Iterating through string:")
for ch in text:
    print(ch)

# List iteration
numbers = [10, 20, 30, 40, 50]
print("\nIterating through list:")
for num in numbers:
    print(num)

# Dictionary iteration
student = {"name": "Ravi", "age": 20, "course": "BCA"}
print("\nIterating through dictionary:")

# Keys
print("Keys:")
for key in student:
    print(key)

# Values
print("\nValues:")
for value in student.values():
    print(value)

# Key-Value pairs
print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)