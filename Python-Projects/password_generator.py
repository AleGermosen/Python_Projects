### Password Generator

# User input criterias like length, the inclusion of uppercase letters, numbers, and special characters.
# Generate random characters equal to the length inserted by user.
# Print generated password.

import string
import random

def password_generator():
    password_length = int(input("Enter password length: "))

    include_uppercase = "y" # (input("Include uppercase letters? (y/n): ")).lower()
    include_numbers = "y" # (input("Include numbers? (y/n): ")).lower()
    include_special_char = "y" # (input("Include special charaters? (y/n): ")).lower()
    
    special_characters = list(string.punctuation) # List of common special characters
    uppercase_characters = list(string.ascii_uppercase)
    lowercase_characters = list(string.ascii_lowercase)
    numbers = list(string.digits)

    password_generated = []
    options_list = ["lower"]

    if include_uppercase == "y":
        options_list.append("upper")
    if include_numbers == "y":
        options_list.append("num")
    if include_special_char == "y":
        options_list.append("special")

    for index in range(password_length):
        random_choice = random.choice(options_list)
        if random_choice == "lower":
            password_generated.append(random.choice(lowercase_characters))
        elif random_choice == "upper":
            password_generated.append(random.choice(uppercase_characters))
        elif random_choice == "num":
            password_generated.append(random.choice(numbers))
        elif random_choice == "special":
            password_generated.append(random.choice(special_characters))

    joined_password = ''.join(password_generated)
    print(f"Generated password: {joined_password}")
