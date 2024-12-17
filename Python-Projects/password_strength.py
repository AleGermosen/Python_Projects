### Password Strength Checker

# User input a password
# Check criterias like length, the inclusion of uppercase letters, numbers, and special characters
# Print the category of the password as Very Weak, Weak, Medium, Strong, or Very Strong.

import string

def password_strength_checker():
    user_password = input("Enter a password: ") # user_password = "P@ssw0rd!"
    user_list = list(user_password)
    
    special_characters = list(string.punctuation) # List of common special characters
    uppercase_characters = list(string.ascii_uppercase)
    numbers = list(string.digits)

    categories = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    select_category = 0

    if len(user_password) > 10:
        select_category += 1

    for index in user_list:
        if index in special_characters:
            select_category += 1
        elif index in uppercase_characters:
            select_category += 1
        elif index in numbers:
            select_category += 1
    
    try:
        print(f"Password stength: {categories[select_category]}")
    except IndexError:
        print(f"Password stength: {categories[4]}")

    if (select_category < 2):
        print("Try using uppercase characters, numbers or special characters like:\n",string.punctuation)