# 2.3 Use Objects and Methods

# -------------------------------
# Example 1
# -------------------------------

# As python is and OOP language information is stored and objects
# for example strings. Objects can effected by the application of
# methods which are denoted via object.method()
# string objects can utilize a number of methods eg .upper() and .lower()

inside_voice = "Can you hear me yet?"
shouting_voice = inside_voice.upper()

print(shouting_voice)

# be quiet people are trying to sleep
print(shouting_voice.lower())

# methods are just functions that belong to objects

# -------------------------------
# Example 2
# -------------------------------

# To make our programs more interactive we can ask the user for input()
# the input() function can take a string to give the user instructions

user_input = input("Give me something please? \n")

print("Thank you people usually just ignore me.")
print("Here's what you said: ", user_input)
print("That's all i can really do no wonder people ignore me")

user_input = input("He wait maybe Is can do something else too! I like yelling, \
Do you like yelling? \nGive me something to yell! \n")
print(user_input.upper())
