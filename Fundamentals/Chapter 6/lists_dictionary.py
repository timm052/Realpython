# lists_dictioarys

# -------------------------------
# Example 1
# -------------------------------

# lists are an object type that is able to hold other objects inside of them
colours = ["red", "green", "burnt sienna", "blue"]
scores = [10, 8, 9, -2, 9]
my_list = ["one", 2, 3.0]  # lists can hold more than one type of object

# getting a value out of a list is similar to getting a character form a string
print(colours[2])
print(colours[1:3])
print(colours)

# lists are multible which means we can change objects in the list
colours[3] = "value changed"
print(colours)

# we can also also add/remove objects to aaready existing lists and create empty
animals = []
animals.append("lion")      # adding objects
animals.append("tiger")
animals.append("happy")
animals.remove("happy")     # removing objects
animals.extend(["cow", "dog", "bird"])  # add mutiple items to a list
print(animals)

# the index() method can be used to find the index of a value in a list
print(colours.index("green"))


# -------------------------------
# Example 2
# -------------------------------

# copying the contents of one list to anouther is more complicated simply
# refrencing anouther list will not create a new list but rather a pointer to
# animals list
large_cats = animals
print(animals)
animals.append("this should not be here")
print(large_cats)

# to copy the contents of a list to a new object we need to retrive all obejcts
# in the  list and add them individualy
large_cats = animals[:]     # method 1
large_cats.extend(animals)  # method 2
print(large_cats)
print(animals)

# since lists are mutible we don't need to reddefine lists when we proform a
# method or function on them
# animals = animals.sort() will destroy the list
animals.sort()
print(animals)

# lists can hold other lists and can be called by using two index refrences
two_by_two = [[1, 3], [2, 4]]
print(two_by_two[1][1])  # returns a specific value
print(two_by_two[1])  # returns a list
two_by_two = ["test", [2, 4]]  # a list is just anouther type of object

# to create a list from a single string use a sybol to define each string
split_test = "happy, sad, bad, dog, cat, crazy"
split_list = split_test.split(", ")
print(split_list)


# *******************************
# Exercises
# *******************************

# Ex 1
desserts = ["ice cream", "cookies"]

# Ex 2
desserts.sort()
print(desserts)

# Ex 3
print(desserts.index("ice cream"))

# Ex 4
food = desserts[:]

# Ex 5
food.extend(["broccoli", "turnips"])

# Ex 6
print(desserts)
print(food)

# Ex 7
food.remove("cookies")
print(food)

# Ex 8
print(food[0:2])

# Ex 9
cookies = "cookies, cookies, cookies"
breakfast = cookies.split(", ")
print(breakfast)

# Ex 10
numbers = [2, 4, 8, 16, 32, 64]


def number_select(list):
    temp_n = []
    for num in list:
        if num >= 1 and num <= 20:
            temp_n.append(num)
    return temp_n

print(number_select(numbers))
