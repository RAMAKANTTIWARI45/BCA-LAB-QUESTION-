try:
    # Taking input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2

    # List
    my_list = [10, 20, 30]

    # Convert float to int
    index = int(result)

    print("Accessing element:", my_list[index])
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input! Please enter integers only.")

except IndexError:
    print("Error: List index out of range.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program execution finished.")