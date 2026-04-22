# Open the file in read mode
file = open("newfile.txt", "r")

# 1. Using read() - reads entire file
print("Using read():")
content = file.read()
print(content)

# Move cursor back to beginning
file.seek(0)

# 2. Using readline() - reads one line at a time
print("\nUsing readline():")
line1 = file.readline()
line2 = file.readline()
print("Line 1:", line1)
print("Line 2:",line2)

# Move cursor back to beginning
file.seek(0)

# 3. Using readlines() - reads all lines as a list
print("\nUsing readlines():")
lines = file.readlines()
print(lines)

# Close the file
file.close()