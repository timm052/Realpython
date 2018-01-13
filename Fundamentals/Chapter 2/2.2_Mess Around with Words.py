# 2.2 Mess Around with Words

# ------------------------------
# Example 1
# ------------------------------

# The length of a string can be determined by using the len() command
my_string = "abc"
string_length = len(my_string)

print(string_length)


# len measures the number of charcaters including spaces
my_string = "ab c"
string_length = len(my_string)
print(string_length)


# -------------------------------
# Example 2
# -------------------------------

# sterings can be added together to create a single string
# This is called concatenating them
string1 = "This is one half of a statement"
string2 = "This is the other other half of the statement"

full_string = string1 + " and " + string2

print(string1)
print(string2)
print(full_string)
# we can even do it in a print function
print("This is a test" + " and " + "this is a second test")
# If we add commas between the strings we want to combines then
# it will automaticlly add spaces between the strings
print("This is a test", "and", "this is a second test")


# -------------------------------
# Example 3
# -------------------------------

# rather than only dealing with the entire string all at once
# we can use single letters from within the string this is known
# as splicing??
alphabet = "abcdefghijklmnopqrstuvwxyz"

# the first character has an index of zero so 3 will extract the 4th char
# a b c d
# 0 1 2 3
print(alphabet[3])
print(alphabet[0])

# we can extract a range of index's from a string
print(alphabet[1:3])
# if we don't specify a start or an end point python will extract all
# chars to the end of the string in that direction
print(alphabet[:3])
print(alphabet[2:])
print(alphabet[:])

# NOTE: python strings are immutible and cannot be changed once created
# to change the data inside a string veriable wou must define a new
# veriable and add the conntents of the old string
