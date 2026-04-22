#arithimatics operation taking input from users

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division carefully (avoid division by zero)
if num2 != 0:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2
else:
    division = "Undefined (division by zero)"
    modulus = "Undefined"

# Exponentiation
power = num1 ** num2

# Display results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Power:", power)