# 3.1 Streamline your print statements

# -------------------------------
# Example 1
# -------------------------------

# String interpolation is a the insertion of date into
# a string

name = "Zaphod"
num_heads = 2
num_arms = 3

# Method 1
# function conversion and comma seperation to automatically ad spaces
print(name, "has", str(num_heads), "heads and", str(num_arms), "arms")

# Method 2
# adding strings together this requires spaces in appropriate places in
# in the strings or manual insertion of space string in the print statement
# making the data messy
print(name + " has " + str(num_heads) +
      " heads and " + str(num_arms) + " arms")

# Method 3
# the above methods can be annoying to read the format() method to insert vars
print("{} has {} heads and {} arms".format(name, num_heads, num_arms))

# index values can be used to select the variables used at for each section
print("{1} has {0} heads and {2} arms".format(num_heads, name, num_arms))

# we can also create objects in the format function
print("{1} has {0} heads and {num_arms} arms".format(
    num_heads, name, num_arms=5))

# In python 3.6 there is a new type of string called a formatted string
# literal which can use previously defined variables and other code
test = "test value"
number = 8
print(
    f"You should see a {test} here followed by a test number here {number+1}")


# **********************************
# Exercises
# **********************************

# Ex 1
weight = 0.2
animal = 'newt'

print(str(weight), "kg is the weight of the", animal)


# Ex 2
print("{} kg is the weight of the {}".format(weight, animal))


# Ex 3
print("{1} kg is the weight of the {0}".format(animal, weight))

# Ex 4
print("{weight} kg is the weight of the {animal}".format(
    animal='newt', weight=0.2))

# Ex 5
print(f"{weight} kg is the weight of the {animal}")
