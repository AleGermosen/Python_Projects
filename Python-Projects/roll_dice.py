### Dice Rolling Game ###

# Loop
    # Ask: roll the dice?
    # If user enter y
        # Generate two random numbers
        # Print them
    # If user enters n
        # Print thank you message
        # Terminate
    # Else
        # Print invalid choice

"""
import random

def roll_dice():
    answer = input("Roll the dice? (y/n): ")
    # while (answer.upper != "N"):
    if answer.upper() == "Y":
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        print (f"({first}, {second})")
    elif answer.upper() == "N":
        print("Thanks for playing!")
    else:
        print("Invalid choice!")
"""

### Dice Rolling Game - Optional Enhancements ###
import random 

def roll_dice_enhanced():
    count_rolls = 0

    while True:
        answer = input("Roll the dice? (y/n): ").upper()
        if answer == "Y":
            variables = {}
            repeat_roll = int(input("How many times would you like to roll the dice?"))
            for i in range(1, repeat_roll + 1):
                count_rolls += 1
                variables[f"dice #{i}"] = random.randint(1, 6)
            for key, value in variables.items():
                print(f"{key}: {value}")
        elif answer == "N":
            print(f"Thanks for playing {count_rolls} times!")
            break
        else:
            print("Invalid choice!")