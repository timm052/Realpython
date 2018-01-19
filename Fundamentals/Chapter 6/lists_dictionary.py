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

#lists are multible which means we can change objects in the list
colours[3] = "value changed"
print(colours)

# we can also also add/remove objects to aaready existing lists and create empty
animals = []
animals.append("lion")      # adding objects
animals.append("tiger")
animals.append("happy")
animals.remove("happy")     # removing objects
animals.extend(["cow", "dog" , "bird"]) # add mutiple items to a list
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
