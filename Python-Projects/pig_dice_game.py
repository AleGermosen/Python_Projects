### Pig Dice Game

# Define players
# Each player should be able to roll a dice
# After one roll, ask the player if he/she wants to continue
# If he/she doesnt want to continue, save the amout of points accumulated
# If the dice is 1, the players loses all the points from the round and must pass the dice
# First player to reach a certain amount wins

import random
current_score_list = []

def roll_dice():
    global dice
    dice = random.randint(1, 6)
    print(f"You rolled a {dice}")
    current_score_list.append(dice)
    return sum(current_score_list)

def pig_dice_game():
    amount_players = 2 # int(input("How many players are going to play? "))
    players_score = {key: 0 for key in range(amount_players)}

    for key in players_score:
        print(f"Player {key + 1}'s turn")
        current_score = roll_dice()
        while True:
            answer = input("Roll the dice? (y/n): ").upper()
            if answer == "Y":
                current_score = roll_dice()
            elif answer == "N":
                try: 
                    players_score.update({key: current_score})
                except UnboundLocalError:
                    current_score = dice
                print(f"Player {key + 1}'s previous score was {current_score}")
                current_score_list.clear()
                break
            else:
                print("Invalid choice!")


# pig_dice_game()