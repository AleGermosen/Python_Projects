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
"""
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
"""

### QR Code Generator

# Enter list to generate codes
# Choose color for the code
# Enter filename
# Save code as an image
"""
import qrcode

def qr_code_generator():
    prompt_text = input("Enter a list of items separated by commas: ")
    prompt_text = prompt_text.split(",")
    total_items = len(prompt_text)
    
    prompt_filename = (input("Enter the base filename: "))
    prompt_color_1 = (input("Enter primary color: ")).lower()
    prompt_color_2 = (input("Enter secondary color: ")).lower()

    count_items = 0
    while (count_items < total_items):
        # Create a QR Code object
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in pixels
            border=4,  # Thickness of the border (minimum is 4)
        )

        # Add data to the QR Code
        qr.add_data(prompt_text[count_items])
        qr.make(fit=True)

        # Create an image of the QR Code
        img = qr.make_image(fill_color=prompt_color_1, back_color=prompt_color_2)

        # Save the QR Code image
        img.save(f"{prompt_filename}_{count_items}.png")
        print(f"QR Code saved as '{prompt_filename}_{count_items}.png'")

        count_items += 1
"""

### Currency Converter

# # User imputs:
# Amount to convert
# Source and Target currency from given options
# Fixed conversion from source to target
# Display currency converted in multiple currencies
# Display a history of conversions
"""
nested_dict = {
    "USD": {'EUR': 0.95, 'CAD': 1.40, 'GBP': 0.79},
    "EUR": {'USD': 1.06, 'CAD': 0.68, 'GBP': 0.83},
    "CAD": {'USD': 0.71, 'EUR': 1.48, 'GBP': 0.56},
    "GBP": {'USD': 1.27, 'EUR': 1.20, 'CAD': 1.78}
}

def get_user_input():
    amount_to_convert = float(input("Enter the amount: "))
    source_currency = (input("(USD/EUR/CAD/GBP): ")).upper()
    target_currency = (input("(USD/EUR/CAD/GBP), separated with commas: ")).upper()
    target_currency = target_currency.split(",")
    return amount_to_convert, source_currency, target_currency


def convert_to_currency(d, amount_to_convert, source_currency, target_currency):    
    conversion = []
    
    count_items = 0
    total_items = len(target_currency)
    while (count_items < total_items):
        target = d[source_currency][target_currency[count_items]]
        convert = amount_to_convert * target
        conversion.append(convert)
        count_items += 1
    return conversion

def currency_converter():
    user_amount, user_source, user_target = get_user_input()
    user_conversion = convert_to_currency(nested_dict, user_amount, user_source, user_target)
    
    count_items = 0
    total_items = len(user_target)
    while (count_items < total_items):
        converted_currency = user_conversion[count_items]
        print(f"{user_amount} {user_source} is equal to {converted_currency} {user_target[count_items]}")
        count_items += 1
"""

### Quiz Game

# import data from an excel
# display question amd options
# user input
# display correct or wrong
# diplay next question and others
# final score 

import pandas as pd

# Load the Excel file
file_path = "quiz.xlsx"
quiz_data = pd.read_excel(file_path)

# Convert the data into a list of dictionaries
quiz = quiz_data.to_dict(orient="records")

"""
quiz = [
    {
        "question": "What is the capital of France?",
        "choices": ["a) Paris", "b) London", "c) Rome"],
        "answer": "a"
    },
    {
        "question": "What is the largest planet in out solar system?",
        "choices": ["a) Earth", "b) Jupiter", "c) Mars"],
        "answer": "b"
    }
]
"""

# Function to check the answer
def check_answer(question_data, user_choice):
    return user_choice.strip().lower() == question_data["Answer"]

def quiz_game():
    count_score = 0
    for q in quiz:
        print(q["Question"])
        choices = q["Choices"].split(";")  # Split choices into a list
        for choice in choices:
            print(choice)  # Print each choice
        # for choice in q["Choices"]:
            # print(choice)
        user_choice = input("Your answer (a/b/c): ")
        if check_answer(q, user_choice):
            print("Correct!")
            count_score += 1
        else:
            print("Wrong!")
    print(f"Your final score: {count_score}/2")


if __name__ == '__main__': 
    # roll_dice()
    # roll_dice_enhanced()
    # guess_number()
    # r_p_s_game()
    # qr_code_generator()
    # currency_converter()
    quiz_game()