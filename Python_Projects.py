###### Python Projects for Beginners by Mosh ######

### Dice Rolling Game ###

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

# Mosh solution
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

while True:
  choice = input('Roll the dice? (y/n): ').lower()
  if choice == 'y':
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')
"""

### Dice Rolling Game - Optional Enhancements ###
"""
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
        else:
            print("Invalid choice!")
            """

### Number Guessing Game ###

# randomly select a number between 1 and 100
# prompt the player to guess the number
# hints if the guess is too high or too low
"""
import random

def guess_number():
    count_tries = 0
    max_tries = 3

    guess_low = int(input("Enter minimum number: "))
    guess_high = int(input("Enter maximum number: "))
    rand_number = random.randint(guess_low, guess_high) # (1, 100)

    while (count_tries < max_tries): #True:
        count_tries += 1
        prompt_guess = int(input(f"Guess the number between {guess_low} and {guess_high}: ")) # 1 and 100: "))
        if ((prompt_guess == rand_number) and (count_tries == 1)):
            print (f"Congratulations! You guessed the number in {count_tries} attempt.")
            break
        elif (prompt_guess == rand_number):
            print (f"Congratulations! You guessed the number in {count_tries} attempts.")
            break
        elif ((prompt_guess > rand_number) and (count_tries < max_tries)):
            print ("Too high! Try again.")
        elif ((prompt_guess < rand_number) and (count_tries < max_tries)):
            print ("Too low! Try again.")
        elif (prompt_guess > rand_number):
            print ("Too high!")
        else: # if (prompt_guess < rand_number):
            print ("Too low!")
    else:
        print(f"Too many tries! The number was {rand_number}.")
        """

### Rock, Paper, Scissors Game ###

# Prompt player to choose rock, paper or scissors
# Computer randomly selects its choice
# Display both choices
# Determine winner
# Make it a 2 out of 3 wins
# Count how many wins the player has
# Add a choice for two players

import random

def r_p_s_game():
    # count_plays = 0
    count_wins_player_1 = 0
    count_wins_player_2 = 0
    count_wins_compu = 0
    total_wins = 2
    letters = ["R", "P", "S"]

    player_or_compu = int(input("Want to play against a computer (1) or another player (2): "))

    if player_or_compu == 1:
        while (count_wins_player_1 < total_wins and count_wins_compu < total_wins):
            prompt_guess = (input("(R)ock, (P)aper, or (S)cissors? ")).upper()
            compu_choice = random.choice(letters)
            print (compu_choice)
            if (prompt_guess == compu_choice):
                print("Tie!")
            elif (prompt_guess == "R" and compu_choice == "P"):
                count_wins_compu += 1
                print ("Computer wins!")
            elif (prompt_guess == "R" and compu_choice == "S"):
                count_wins_player_1 += 1
                print ("Player wins!")
            elif (prompt_guess == "P" and compu_choice == "S"):
                count_wins_compu += 1
                print ("Computer wins!")
            elif (prompt_guess == "P" and compu_choice == "R"):
                count_wins_player_1 += 1
                print ("Player wins!")
            elif (prompt_guess == "S" and compu_choice == "R"):
                count_wins_compu += 1
                print ("Computer wins!")
            elif (prompt_guess == "S" and compu_choice == "P"):
                count_wins_player_1 += 1
                print ("Player wins!")
            else:
                print("Wrong letter was selected, try again!")
        print ("Game Over!")
        print(f"Computer won {count_wins_compu} times.")
        print(f"Player won {count_wins_player_1} times.")
    elif player_or_compu == 2:
        while (count_wins_player_1 < total_wins and count_wins_player_2 < total_wins):
            prompt_guess = (input("Player 1: (R)ock, (P)aper, or (S)cissors? ")).upper()
            prompt_guess_2 = (input("Player 2: (R)ock, (P)aper, or (S)cissors? ")).upper()
            if (prompt_guess == prompt_guess_2):
                print("Tie!")
            elif (prompt_guess == "R" and prompt_guess_2 == "P"):
                count_wins_player_2 += 1
                print ("Player 2 wins!")
            elif (prompt_guess == "R" and prompt_guess_2 == "S"):
                count_wins_player_1 += 1
                print ("Player 1 wins!")
            elif (prompt_guess == "P" and prompt_guess_2 == "S"):
                count_wins_player_2 += 1
                print ("Player 2 wins!")
            elif (prompt_guess == "P" and prompt_guess_2 == "R"):
                count_wins_player_1 += 1
                print ("Player 1 wins!")
            elif (prompt_guess == "S" and prompt_guess_2 == "R"):
                count_wins_player_2 += 1
                print ("Player 2 wins!")
            elif (prompt_guess == "S" and prompt_guess_2 == "P"):
                count_wins_player_1 += 1
                print ("Player 1 wins!")
            else:
                print("Wrong letter was selected, try again!")
        print ("Game Over!")
        print(f"Player 1 won {count_wins_player_1} times.")
        print(f"Player 2 won {count_wins_player_2} times.")
    else:
        print("Wrong choice, run program again.")


if __name__ == '__main__': 
    # roll_dice()
    # roll_dice_enhanced()
    # guess_number()
    r_p_s_game()