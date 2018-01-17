# Break out of pattern

# There are two main keywords that help to control the flow of programs
# in Python: break and continue. They are used in combination with for
# and while.

# break breaks out of a loop when break appears
for i in range(0, 4):
    if i == 2:
        break
    print(i)

print("Finished with i = ", str(i))

# continue jumps to the end of the loop but keeps the loop running here we
# skip over the print statement for the second loop interation.
for i in range(0, 8):
    if i == 2:
        continue
    print(i)

print("Finished with i = ", str(i))


# -------------------------------
# Example 2
# -------------------------------

# Loops can have else staments in python else staments will exectute when a loop
# ends naturally and not as a result of a break
phrase = "this is a test string"

for letter in phrase:
    if letter == "X":
        break
else:
    print("There was no 'X' in the phrase")


# *******************************
# Exercises
# *******************************

# Ex 1
string = input(
    "Enter a letter or string to try and esacape this pugatory hell: ")
escape = False
exit_strings = ["Q", "q", "quit", "Quit", "exit", "Exit"]

while True:
    for i in exit_strings:
        if string == i:
            escape = True

    if escape == True:
        break
    else:
        string = input("There is no escape enter anouther string Mahahaha: ")

# Ex 2
print("Below is list of all number from 1 to 50 that are not multiples of 3")
for i in range(1, 51):
    test = i
    test = 3%test

    if test == 0:
        continue
    print(i)
