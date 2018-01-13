# 3.4 Find a string in a string

# -------------------------------
# Example 1
# -------------------------------

# the find() method can be used to find the location of a string within another
# string the method is applied to the object using dot notation because
# the method belongs to the string object.
phrase = "the surprise is here somewhere, surprise"

# the find method will find the index of the the first letter occurrence of the
# searched string
print(phrase.find("surprise"))

# if it fails to find the string it will return -1
print(phrase.find("apples"))

# NOTE: The matching is exact an case sensitive and can only be applied to
# strings using strings

# -------------------------------
# Example 2
# -------------------------------

# a similar method is the replace() method which replaces all occurrences of a
# string with another string
story = "This is a grand tale about lies and truth"

print(story)
print(story.replace("truth", "more lies"))

# NOTE: calling the method does not actually change the value of story in
# order for that to occur you need to redefine the variable

# *******************************
# Exercises
# *******************************

# Ex 1
print("AAA".find("a"))

# Ex 2
version = "version 2.0"
search_value = 2.0

print(version.find(str(search_value)))

# Ex 3
letter = input(
    "This script will display the index of the first occurrence of the letter a in the statement you enter. \n")

print(letter.find("a"))
