# Dictionary operations program

# Creating a dictionary
student = {
    "name": "Ravi",
    "age": 20,
    "course": "BCA"
}

print("Original Dictionary:", student)

# Add a new key-value pair
student["city"] = "Bhopal"
print("\nAfter adding (city):", student)

# Update existing value
student["age"] = 21
print("After updating (age):", student)

# Delete an element using del
del student["course"]
print("After deleting (course):", student)

# Delete using pop()
student.pop("city")
print("After pop (city):", student)