# simulate events and calc probs

# -------------------------------
# Example 1
# -------------------------------

# Run a simulation using a Monte Carlo experiment to do this we
# need to add chance to the code using the built in random module

# Modules are a collection of funtions and need to be imported to be used
# we onlt need to import one function randint()
from random import randint

# randint(x, y) gives a random rumber between x and y
print(randint(0, 15))


# -------------------------------
# Example 2
# -------------------------------

# this can be used to simulate the ratio of heads to tails in a coin flip
heads = 0
tails = 0

for trials in range(0, 10000):  # determines number of trials
    trial = randint(0, 1)
    if trial == 0:
        tails = tails + 1
    else:
        heads = heads + 1

print(f"heads / tails = {heads/tails}")
print(f"over {heads + tails} trails")


# *******************************
# Exercises
# *******************************

# Ex 1
print(f"The dice rolled: {randint(1, 6)}")

# Ex 2
no_trials = 10000
temp = 0
i = 0

for trails in range(0, no_trials):
    trial = randint(1,6)
    temp += trial
    i += 1

print(f"The average result from {no_trials} tosses is {temp/i}")
