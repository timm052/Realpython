# Recover from errors

# -------------------------------
# Example 1
# -------------------------------

# a common error is trying to convert a string to a number when there is
# no numerical content in the string. To prevent this we can use a try/except
# pair which will stop the code from breaking.
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer.")


# the try block runs normally and if no error occurs the code skips the except
# block. Should there be a ValueError the except block runs multiple errors can
# be handled by a single except block this is not used commonly as code should
# react diffrently when it encounters diffrent kinds of errors
def divide(num1, num2):
    '''devides one number by anouther number with type checking and
    dev/0 protection'''
    try:
        print(num1 / num2)
    except (TypeError):
        print("Error wrong type please enter a number")
    except (ZeroDivisionError):
        print("Can't divide by zero")


divide("test", "10")
divide(10, 0)
divide(10, 20)


# *******************************
# Exercises
# *******************************

#Ex 1
while True:
    try:
        number = int(input("Input an integer: "))
        break
    except (TypeError, ValueError):
        print("The data you entered is not an integer")

print(f"The integer you entered was {number}")
