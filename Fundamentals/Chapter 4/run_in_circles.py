# Running in circles

# loops are used to repeat a section of code until a condition chnages from
# True to False or a spceified number of loops are done. There are two types
# of loops in python for and while loops

# -------------------------------
# Example 1
# -------------------------------

# While loops execute while a specified variable or condition remains true.
n = 1

while (n < 5):
    print(f"n = {n}")
    n = n + 1

print("loop complete")

# NOTE: it is easy to get stuck in an infinite loop if the condition is always
# True


# -------------------------------
# Example 2
# -------------------------------

# a for loop will loop a specfided number of times based on either an iterator
# or the number of values in a list. The range function is used here to create
# a list of numbers and will loop for each value.

for n in range(1, 5):
    print(f"n = {n}")

print("loop complete")

# NOTE: the range function starts at the first number specified but finishes 1
# number before the end on the range.


# -------------------------------
# Example 3
# -------------------------------

# the code below show nesting a loop within anouther loop the nested loop shows
# an example of using a for loop to loop over a list of content. The main loop
# will execute 3 times while the nested loop will loop 3 time for each loop of
# the main loop for a total of 9 times.
for n in range(1, 4):
    for j in ["a", "b", "c"]:
        print(f"n = {n} and j = {j}")
print()


# *******************************
# Excercises
# *******************************

# Ex 1
for x in range(2, 11):
    print(f"x = {x}")
print()

# Ex 2
n = 2
while n <= 10:
    print(f"n = {n}")
    n += 1
print()


# Ex 3
def doubles(num):
    for x in range(1, 4):
        num = num + num
        print(num)


doubles(2)
