# 4.0 Functions and Loops

# -------------------------------
# Example 1
# -------------------------------

# numerical calculations can be carried out in strings using formated strings
print(f"1 + 1 = {1+1}")
print(f"2 X (2 + 3) = {2 * (2 + 3)}")
print(f"1.2 / 0.3 = {1.2/0.3}")
print(f"5 / 2 = {5/2}")


# -------------------------------
# Example 2
# -------------------------------

# functions act and miniture programs that can be reused and applied to
# multible sections of code easily and without duplicating large sections
# of code. This improves readability and the amount of conding required
# python uses def to define a new function.
def square(number):
    sqr_num = number ** 2
    return sqr_num


# simply creating a definition will not cause it to run when the program is
# run. The function needs to be called and returned value prined if the
# fucntion does not already contain a print function
input_num = 5

print(square(input_num))

# NOTE: the fucntion must be defined or imported before
# it is called in the script


# functions can take multiple input values
def return_diffrence(num1, num2):
    """ Returns the diffrence between n1 and n2 """
    return num1 - num2


print(return_diffrence(3, 5))

# NOTE: functions can include documations known as doc strings which will will
# provide aditional infomation about the function when using help()

print(help(return_diffrence))


# ****************************
# Exercises
# ****************************

# Ex 1
def cube(number):
    return number * number * number


print(cube(10))
print(cube(12))
print(cube(23))
print(cube(4))


# Ex 2
def multi(num1, num2):
    return num1 * num2


print(multi(10, 20))
print(multi(7, 2))
print(multi(5, 6))
print(multi(3, 20))
