# Q19: Copy file

src = open("newfile.txt", "r")
data = src.read()

dest = open("copy.txt", "w")
dest.write(data)

src.close()
dest.close()

file = open("copy.txt", "r")
print(file.read())
file.close()