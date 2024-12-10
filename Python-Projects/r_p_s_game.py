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