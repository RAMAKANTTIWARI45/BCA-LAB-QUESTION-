
# Taking input from user
num = float(input("Enter a number: "))

# Nested if to classify number
if num >= 0:
    if num == 0:
        print("The number is Zero")
    else:
        print("The number is Positive")
else:
    print("The number is Negative")