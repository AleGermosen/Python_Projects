### Quiz Game

# import data from an excel
# display question amd options
# user input
# display correct or wrong
# diplay next question and others
# final score 

import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "quiz.xlsx")

# Load the Excel file
import pandas as pd
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