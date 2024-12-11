### Tic Tac Tpe Game

# Make a list that mark the positions
# Create a grid 
# Two players take turn with different colors for each player
# Display grid after each move
# Check who wins or if it's a draw
# Display which player wins

print("""
--------+-------+--------
    1   |   2   |   3
--------+-------+--------
    4   |   5   |   6
--------+-------+--------
    7   |   8   |   9
--------+-------+--------
             """)

def tic_tac_toe_game():
    num_list = list(range(9))
    list_grid = [str(num) for num in num_list]
    
    while True:
        player_1 = int(input("Player O's turn, enter position: "))
        player_2 = int(input("Player X's turn, enter position: "))

        list_grid[player_1] = "O"
        list_grid[player_2] = "X"

        try:
            num_list.remove(player_1)
        except ValueError:
            print("Space is already occupied.")

        try:
            num_list.remove(player_2)
        except ValueError:
            print("Space is already occupied or game is tied.")

        grid = (f"""
    --------+-------+--------
        {list_grid[0]}   |   {list_grid[1]}   |   {list_grid[2]}
    --------+-------+--------
        {list_grid[3]}   |   {list_grid[4]}   |   {list_grid[5]}
    --------+-------+--------
        {list_grid[6]}   |   {list_grid[7]}   |   {list_grid[8]}
    --------+-------+--------
    """)
        
        print(grid)

        # Horizontal
        if ((list_grid[0] == "O" and list_grid[1] == "O" and list_grid[2] == "O") 
            or (list_grid[3] == "O" and list_grid[4] == "O" and list_grid[5] == "O")  
            or (list_grid[6] == "O" and list_grid[7] == "O" and list_grid[8] == "O")):
            print("Player 1 wins!")
            break
        elif ((list_grid[0] == "X" and list_grid[1] == "X" and list_grid[2] == "X")
            or (list_grid[3] == "X" and list_grid[4] == "X" and list_grid[5] == "X")  
            or (list_grid[6] == "X" and list_grid[7] == "X" and list_grid[8] == "X")):
            print("Player 2 wins!")
            break

        # Vertical
        elif ((list_grid[0] == "O" and list_grid[3] == "O" and list_grid[6] == "O") 
            or (list_grid[1] == "O" and list_grid[4] == "O" and list_grid[7] == "O")  
            or (list_grid[2] == "O" and list_grid[5] == "O" and list_grid[8] == "O")):
            print("Player 1 wins!")
            break
        elif ((list_grid[0] == "X" and list_grid[3] == "X" and list_grid[6] == "X")
            or (list_grid[1] == "X" and list_grid[4] == "X" and list_grid[7] == "X")  
            or (list_grid[2] == "X" and list_grid[5] == "X" and list_grid[8] == "X")):
            print("Player 2 wins!")
            break

        # Diagonal
        elif ((list_grid[0] == "O" and list_grid[4] == "O" and list_grid[8] == "O") 
            or (list_grid[6] == "O" and list_grid[4] == "O" and list_grid[2] == "O")):
            print("Player 1 wins!")
            break
        elif ((list_grid[0] == "X" and list_grid[4] == "X" and list_grid[8] == "X")
            or (list_grid[6] == "X" and list_grid[4] == "X" and list_grid[2] == "X")):
            print("Player 2 wins!")
            break
        elif len(num_list) == 0:
            print("Tie Game!")
            break
        else:
            continue
    print("Game Over!")


tic_tac_toe_game()