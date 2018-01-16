# Flow of Program

# -------------------------------
# Example 1
# -------------------------------

# so far there has been no way to allow decision making using boolens
# combined with if staements to test if conditions are True or not
# if statements will run if the conditions are evaluated to True
if 2 + 2 == 4:
    print("2 and 2 is 4")
    print("Arithmetic works")

# to set multiple if conditions and alternative case if none of the if or elif
# statements are True then the else staement will run. When the code follows
# one path it is known as branching.
num = 15

if num == 15:
    print("Maths is broken")
elif num < 16:
    print("nah it's cool maths seems to work")
    if num + 20 = > 20:
        print("works real well")
else:
    print("yeah I have no idea what's going on")
# NOTE: if there is an elif and if statement and both are true on the if
# statement will execute. Also else and elif statements are optional
