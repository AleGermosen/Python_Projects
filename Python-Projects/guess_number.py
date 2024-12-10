### Number Guessing Game ###

# randomly select a number between 1 and 100
# prompt the player to guess the number
# hints if the guess is too high or too low

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