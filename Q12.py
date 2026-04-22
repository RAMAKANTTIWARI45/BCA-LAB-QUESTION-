# Program for list slicing and manipulation

# Creating a list
lst = [10, 20, 30, 40, 50, 60]

print("Original List:", lst)

# List slicing
print("First 3 elements:", lst[0:3])
print("Last 3 elements:", lst[-3:])
print("Every second element:", lst[::2])

# List manipulation
lst.append(70)        # Add element at end
print("After append:", lst)

lst.insert(2, 25)     # Insert at index 2
print("After insert:", lst)

lst.remove(40)        # Remove specific element
print("After remove:", lst)

lst.pop()             # Remove last element
print("After pop:", lst)

lst.sort()            # Sort the list
print("After sort:", lst)

lst.reverse()         # Reverse the list
print("After reverse:", lst)