
# Define a custom exception
class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    num = int(input("Enter a positive number: "))

    # Raise custom exception if number is negative
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

    print("You entered:", num)

except NegativeNumberError as e:
    print("Custom Exception Caught:", e)

except ValueError:
    print("Error: Please enter a valid integer.")

finally:
    print("This block always executes (finally block).")