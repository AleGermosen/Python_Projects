### Word Guessing Game

# Import random word from text file
# User input guess
# Check if the letter is part of the word and place the letter in its place if it is
# If it's not, then count and try again

import os
import random

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "words.txt")
with open(file_path, "r") as file:
    text_data = file.read()

text_data = text_data.split(" ")
text_data = [char.strip('.,') for char in text_data]
text_data = [char.lower() for char in text_data]

empty_spaces_list = []

def word_guessing_game():
    failed_attempt = 0
    max_attemps = 6

    random_choice = random.choice(text_data)
    random_choice_list = list(random_choice)

    for index in range(len(random_choice)):
        empty_spaces_list.append("_")
    empty_spaces = ''.join(empty_spaces_list)
    print(empty_spaces)

    while True:
        letter_found = 0
        user_guess = (input("Enter a letter: ")).lower()

        for position, char in enumerate(random_choice_list):
            if char == user_guess:
                print(f"Found the letter '{user_guess}' in the {position}!")
                empty_spaces_list.pop(position)
                empty_spaces_list.insert(position, user_guess)
                letter_found = 1
        
        empty_spaces = ''.join(empty_spaces_list)
        print(empty_spaces)   

        if letter_found == 0 and failed_attempt < (max_attemps - 1):
            print("Letter is not in the word, try again.")
            failed_attempt += 1
        elif failed_attempt == (max_attemps - 1):
            print("Letter is not in the word, you lost.")
            break     
        
        if "_" not in empty_spaces_list:
            print("Congratulations!")
            break