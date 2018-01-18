# Coin Toss
# simulates a coin being fliped until it displays both heads and tails one
# and records how many times it takes
from random import randint
trials = 10000
number_of_flips = 0

for tests in range(0, trials):
    heads = 0
    tails = 0
    while True:
        flip = randint(0,1)
        if flip == 1:
            heads += 1
        else:
            tails += 1

        if heads != 0 and tails != 0:
            number_of_flips += heads + tails
            break

print(f"{number_of_flips/trials}")
