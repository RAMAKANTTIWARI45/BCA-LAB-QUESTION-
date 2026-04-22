# Create and write data to a file
with open("sample.txt", "w") as file:
    file.write("Hello World!\nWelcome to Python file handling.\n")

# Open file in read mode
with open("sample.txt", "r") as file:
    # Read first 5 characters
    print("Reading first 5 characters:")
    print(file.read(5))

    # Move pointer to beginning using seek(0)
    file.seek(0)
    print("\nAfter seek(0), reading again:")
    print(file.read(5))

    # Move pointer to 6th position
    file.seek(6)
    print("\nAfter seek(6), reading next 5 characters:")
    print(file.read(5))

    # Move pointer to end of file
    file.seek(0, 2)   # 2 means end of file
    print("\nPointer moved to end using seek(0,2)")
    print("Current position:", file.tell())