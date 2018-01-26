from capitals import capitals_dict
import random
import os

continue_playing = True
capital_keys = capitals_dict.keys()
capital_keys = list(capital_keys)
score = 0

while continue_playing == True:
    continue_playing == False
    selected_city = random.choice(capital_keys)
    answer = input(f"What is the state capital of {selected_city}? \n")
    tries = 0

    while True:

        if answer == capitals_dict[selected_city]:
            score += 1
            print()
            print(f"{answer} is Correct \n")
            break
        else:
            print(f"{answer} is Incorrect \n")
            tries = tries + 1
            if tries >= 10:
                continue_playing = input("Would you like to skip this question? Y/N \n")
                if continue_playing == 'Y' or continue_playing == 'y':
                    break
            answer = input(f"\nWhat is the state capital of {selected_city}? \n")


    print(f"Your current score is {score}")
    con_test = input("Would you like to continue playing? Y/N \n")
    if con_test == 'N' or con_test == 'n':
        os.system("cls")
        break
    else:
        continue_playing == True
        os.system("cls")


print(f"Your final score is {score}!")
