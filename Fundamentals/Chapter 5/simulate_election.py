# Election simulator
from random import random

numberOftrails = 10000
candidateAwin = 0
candidateBwin = 0


def vote_tally(chance_of_win):
    if random() < chance_of_win:
        return True
    else:
        return False


for elections in range(0, numberOftrails):
    result = 0

    regionA = vote_tally(.87)
    regionB = vote_tally(.25)
    regionC = vote_tally(.17)
    result = regionA + regionB + regionC

    if result < 2:
        candidateAwin += 1
    else:
        candidateBwin += 1

winA = round((candidateAwin / numberOftrails) * 100, 4)

print(f"Candidate A has a {winA}% chance of winning")
print(f"Candidate B has a {100 - winA}% chance of winning")
