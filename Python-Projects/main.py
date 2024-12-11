### Main app for the projects

# import files
# display options and ask user which app is to be ran
# check if the chosen option is available
# run chosen app

from currency_converter import currency_converter
from guess_number import guess_number
from qr_code_generator import qr_code_generator
from quiz_game import quiz_game
from r_p_s_game import r_p_s_game
from roll_dice import roll_dice_enhanced
from tic_tac_toe_game import tic_tac_toe_game

list_apps = {
    "a": roll_dice_enhanced,
    "b": guess_number,
    "c": r_p_s_game,
    "d": qr_code_generator,
    "e": currency_converter,
    "f": quiz_game,
    "g": tic_tac_toe_game,
}

if __name__ == '__main__':
    print("""
    a) Roll the dice game
    b) Guess the number
    c) Rock, paper, scissors game
    d) QR code generator
    e) Currency converter
    f) Quiz game
    """)
    user_input = input("Which app would you like to run? ").lower()

    if user_input in list_apps:
        list_apps[user_input]()