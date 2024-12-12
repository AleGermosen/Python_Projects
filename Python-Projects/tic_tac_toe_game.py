### Tic Tac Toe Game

# Make a list that mark the positions
# Create a grid 
# Two players take turn
# Display grid after each move
# Check who wins or if it's a draw
# Display which player wins

def tic_tac_toe_game():
    num_list = list(range(9))
    list_grid = [str(num) for num in num_list]

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

    players_dict = {
        "Player 1": "O", 
        "Player 2": "X",
    }
    
    while True:
        for key in players_dict:
            while True:
                try:
                    value = players_dict[key]
                    player_input = int(input(f"Player {value}'s turn, enter position: "))
                    num_list.remove(player_input)
                except ValueError:
                    print("Space is already occupied.")
                    continue
                list_grid[player_input] = value
                break

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
            if ((list_grid[0] == value and list_grid[1] == value and list_grid[2] == value) 
                or (list_grid[3] == value and list_grid[4] == value and list_grid[5] == value)  
                or (list_grid[6] == value and list_grid[7] == value and list_grid[8] == value)):
                print(f"{key} wins!")
                exit()

            # Vertical
            elif ((list_grid[0] == value and list_grid[3] == value and list_grid[6] == value) 
                or (list_grid[1] == value and list_grid[4] == value and list_grid[7] == value)  
                or (list_grid[2] == value and list_grid[5] == value and list_grid[8] == value)):
                print(f"{key} wins!")
                exit()

            # Diagonal
            elif ((list_grid[0] == value and list_grid[4] == value and list_grid[8] == value) 
                or (list_grid[6] == value and list_grid[4] == value and list_grid[2] == value)):
                print(f"{key} wins!")
                exit()

            # Check if board is full
            elif len(num_list) == 0:
                print("Tie Game!")
                exit()