import random

def roll_dice():
    return random.randint(1, 6)

input("Press Enter to roll the dice... ")
dice_result = roll_dice()
print(f"You rolled a {dice_result}!")

#for continuous rolling

import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice (or Ctrl+C to quit)... ")
    print(f"You rolled a {roll_dice()}!")
