# -------- STRING FUNCTIONS --------
def string_operations(s):
    print("\n--- String Operations ---")
    print("Original String:", s)
    print("Length:", len(s))
    print("Uppercase:", s.upper())
    print("Lowercase:", s.lower())
    print("Reversed:", s[::-1])
    print("First 5 characters:", s[:5])


# -------- LIST FUNCTIONS --------
def list_operations(lst):
    print("\n--- List Operations ---")
    print("Original List:", lst)
    print("Length:", len(lst))
    print("Maximum:", max(lst))
    print("Minimum:", min(lst))
    print("Sum:", sum(lst))

    # List manipulation
    lst.append(100)
    print("After append(100):", lst)

    lst.insert(1, 50)
    print("After insert at index 1:", lst)

    lst.remove(lst[0])
    print("After removing first element:", lst)


# -------- MAIN FUNCTION --------
def main():
    # String input
    s = input("Enter a string: ")
    string_operations(s)

    # List input (taking numbers separated by space)
    lst = list(map(int, input("\nEnter list elements (space separated): ").split()))
    list_operations(lst)


# Run program
main()