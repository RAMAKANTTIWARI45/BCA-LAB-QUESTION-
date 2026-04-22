
# 1. Writing data to a file (overwrites if file already exists)

file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This file is created using write mode.\n")
file.close()

# 2. Appending data to the same file
file = open("sample.txt", "a")
file.write("This line is added using append mode.\n")
file.write("Appending more data to the file.\n")
file.close()

# 3. Reading the file to check contents
file = open("sample.txt", "r")
print(file.read())
file.close()