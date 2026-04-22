try:
    # Taking input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integers.")

except Exception as e:
    print("Unexpected error occurred:", e)

finally:
    print("Program execution completed.")