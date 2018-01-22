# tuples

# -------------------------------
# Example 1
# -------------------------------

# tuples are similar to lists the major diffrence being that
# they are immutable and cannot be changed
my_tuple = ("word1", "word2", "word3")
print(my_tuple)

# there are no methods fro tuples but you can still use indexs to call values
print(my_tuple[1])

# tuples are only really useful if we have a list we want to avoid acidentally
# altering such as when a fucntion returns muliple values
def adder_sub(num1, num2):
    add = num1 + num2
    subtract = num1 - num2
    return add, subtract

test = adder_sub(10, 5)
print(type(test))


# -------------------------------
# Example 2
# -------------------------------

# tuples don't actually require () to create creating tuples this way is known
# as tuple packing
position = 4.21, 9.29
print(position)

# we can also unpack tuples into indervidual veriables
x, y = position
print(x)
print(y)


# *******************************
# Exercises
# *******************************

# Ex 1
cardinal_name = ("first", "second", "third")

# Ex 2
print(cardinal_name[1])

# Ex 3
pos1, pos2, pos3 = cardinal_name
print(pos1)
print(pos2)
print(pos2)
