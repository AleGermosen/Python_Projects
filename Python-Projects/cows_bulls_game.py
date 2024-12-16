### Cows and Bulls Game

# Generate random 4-digit number
# User input for the guess
# Print a cow for every digit correct but on the wrong spot
# Print a bull for every digit correct and on the right spot

import random

def cows_bulls_game():
    list_random_number = []
    guesses = 0
    amount_digits = 4 # int(input("How many digits do you want to be generated? "))
    amount_guesses = 3 # int(input("How many times do you want to guess before a hint? "))
    
    for index in range(amount_digits):
        while True:
            random_number = random.randint(1, 6)
            if random_number not in list_random_number:
                list_random_number.append(random_number)
                break
    # print(list_random_number)

    while True:
        cows = 0
        bulls = 0

        user_input = input("Guess: ")
        user_guess = [int(x) for x in user_input]
        guesses += 1

        for index in range(amount_digits):
            if user_guess[index] == list_random_number[index]:
                bulls += 1
            elif user_guess[index] in list_random_number:
                cows += 1
        print(f"{guesses}/{amount_guesses} guesses before receiving a hint")
        print(f"{cows} cows, {bulls} bulls")

        if bulls == amount_digits:
            break
        elif guesses == amount_guesses:
            guesses = 0
            for index in range(amount_digits):
                if user_guess[index] == list_random_number[index]:
                    print(f"The bull you found is {list_random_number[index]}")

    print("You win!")