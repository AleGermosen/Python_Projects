### Slot Machine Game

# User input a starting balance, bet amount, and repeat spin
# Random choice from a list of emojis
# Display amount won if 2 or 3 emojis are the same

import emoji
import random

options_list = [":cherries:", ":bell:", ":four_leaf_clover:", ":lemon:", ":watermelon:"]
selected_options = []

def slot_machine_game():
    start_balance = 100 # int(input("Enter your starting balance: $"))

    print("\nWelcome to the Slot Machine Game!\n")
    print(f"Current balance: ${start_balance}")

    while True:
        bet_scored = 0
        selected_options.clear()
        user_bet = int(input("Enter your bet amount: $"))

        check_available = start_balance - user_bet
        if check_available < 0:
            print("You don't have enough balance.")
            continue

        for i in range(3):
            random_choice = random.choice(options_list)
            selected_options.append(random_choice)
        print(f"{emoji.emojize(selected_options[0])} | {emoji.emojize(selected_options[1])} | {emoji.emojize(selected_options[2])}")

        if selected_options[0] == selected_options[1] and selected_options[0] == selected_options[2]:
            print("You win!")
            bet_scored = user_bet * 10
        elif selected_options[0] == selected_options[1] or selected_options[0] == selected_options[2] or selected_options[1] == selected_options[2]:
            print("You win!")
            bet_scored = user_bet * 2
        else:
            print("You lost!")
            start_balance -= user_bet
        
        start_balance += bet_scored
        print(f"Current balance: ${start_balance}")
        
        if start_balance == 0:
            break 

        while True:
            user_repeat = (input("Do you want to play again? (y/n): ")).lower()
            if user_repeat == "n":
                print(f"Your final balance is ${start_balance}")
                exit()
            elif user_repeat == "y":
                break
            else:
                print("Invalid choice!")