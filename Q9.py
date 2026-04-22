# break, continue, pass

# Demonstration of break, continue, and pass

print("---- break example ----")
for i in range(1, 10):
    if i == 5:
        break   # exits the loop when i becomes 5
    print(i)

print("\n---- continue example ----")
for i in range(1, 10):
    if i == 5:
        continue   # skips the rest of the loop for i = 5
    print(i)

print("\n---- pass example ----")
for i in range(1, 6):
    if i == 3:
        pass   # does nothing (placeholder)
    print(i)