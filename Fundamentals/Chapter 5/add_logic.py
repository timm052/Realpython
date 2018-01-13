# add_logic

# python has a number of keywords for compairing expressions
# and, or and not they not as you wouldd expect

# -------------------------------
# Example 1
# -------------------------------

# and requires both statements to be true for the statement to be true
print(1 < 2 and 5 > 1)  # True
print(1 > 2 and 3 > 4)  # False
print(1 < 2 and 3 > 4)  # False
print(1 > 2 and 3 > 4)  # False
print()

# or returns True if atleast one value is True
print(5 > 1 or 8 > 5)  # True
print(5 > 1 or 3 > 4)  # True
print(1 > 2 or 3 < 4)  # True
print(1 > 2 or 3 > 4)  # False
