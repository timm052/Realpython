# 3.0 Working with Strings

# -------------------------------
# Example 1
# -------------------------------

# While strings can hold numbers, letter and most ASCII characters
# string numbers are different to actual numbers
# Eg. adding the string '2' to '2' as shown below will only concatenate
# the  characters together equaling '22' as shown below
string_number = "2"

print(string_number + string_number)

# We can also multiply strings together which will copy the value the alloted
# number of times
string_number = "23"

print(string_number * 3)


# -------------------------------
# Example 2
# -------------------------------

# String numbers can be converted to real? numbers using the int()
# or float() functions which will convert a string into an int() or
# a string respectively these functions can also be used to convert
# numbers into a  float if they are currently an int or vice versa.
string_number = "59965"
integer_number = int(string_number)
float_number = float(integer_number)
back_to_string = str(float_number)

print("String:", string_number, "fifty nine thousand nine hundred and sixty five")
print("Integer:", integer_number)
print("Float:", float_number)

# Numbers can be converted to strings this useful when concatenating numbers
# and strings for text display and python does not know how to add objects of
# different types together
print("Float2String:", back_to_string + "string")

# NOTE: changing a float into an integer will sacrifice the data
# carried past the decimal place and sting what have decimal places
# cannot be converted into integers

# *****************************
# Exercises
# *****************************

# Ex 1
string_number = "586"
coverted_number = int(string_number)

print(coverted_number * 10)

# Ex 2
string_number = "586.85"
coverted_number = float(string_number)

print(coverted_number * 10)

# Ex 3
string_number = "562"
int_number = 45

print(string_number + str(int_number))
