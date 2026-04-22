#taking the input from users 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
#finding the largest number
if a > b and a > c:
    print("Largest number is:", a)
elif b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)