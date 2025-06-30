from string import ascii_uppercase

BOARD_SIZE = 3
playable_pieces = ["X", "O"]

# Game Board
def create_board(board_size) -> list:

    """
    Create a tic-tac-toe board with the specified size, with grid lines and an index table.

    Args:
        board_size (int): The size of the board (number of rows and columns).

    Returns:
        list: A 2D list representing the game board, where each cell is initialized to "-".
    """
    letter_grid = []
    board = []

    for i in range(board_size):
        row = []
        for col in range(
            board_size * 2 - 1
        ):  # doubles the size of grid to accommodate spacers, and stops one short of adding a third spacer
            if len(row) == 0: # if start of row, insert index + 1 (to not start at zero), along with a space for better visual
                row.append(str(i + 1) + " ")
            if (
                col % 2 == 0
            ):  # checks if dividing the current index of col is zero, if true places a '-', if false, adds a '|'
                row.append(" - ")  # playable space
            else:
                row.append(" | ")  # spacer
        board.append(
            row
        )  # builds the row up until it finishes the for loops, starting the row list over again
    for i in range(board_size):
        letter_grid.append(" ")
        letter_grid.append("  " + ascii_uppercase[i] + "  ")
    
    board.insert(0, letter_grid)
    return board

def draw_board(board):
    """Displays the game board as characters aesthetically"""
    string = ''
    for row in board:
        for char in row:
            string += char
        print(string)
        string = ""
        

# Game Logic

def legal_move(user_piece, user_row, user_col, board):
    """Takes the user inputted string for the chosen row and column, and checks to make sure the move is legal.
    Returns: Boolean"""
    row = int(user_row)
    col_string = "  " + user_col.upper() + "  " 
    if row < 0 or row >= len(board) or col_string not in board[0] : # change
        print('Your move is out of the playable bounds. Please input a valid placement.')
        return False
    
    col = board[0].index(col_string)

    if board[row][col] == ' O ' or board[row][col] == ' X ':
        user_piece = " " + user_piece + " "
        if board[row][col] == user_piece:
            print('You already have a piece there.\n')
            return False
        else:
            print("You can't place a piece over your opponents.\n")
            return False
    else:
        return True

        
def place_piece(user_piece, user_row, user_col, board):
    row = int(user_row)
    col = board[0].index("  " + user_col.upper() + "  ")
    if True:
        board[row][col] = " " + user_piece.upper() + " "
    return board



# win checks

def game_state(board, player):
    if horizontal_win(board, player):
        return True
    if vertical_win(board, player):
        return True
    return False



def horizontal_win(board, player):
    board = [piece.strip() for piece in board if piece == 'X' or piece == 'O']
    print(board)
    for row in board:
        if all(piece.strip() for piece in row):
            print(f"{player}'s has won horizontally!\n")
            return True
    return False

def vertical_win(board, player):
    for col in range(len(board[0])):  # Loop over each column
        vert_win = []  # Reset the vertical win tracker for this column
        for row in range(len(board)):  # Loop through each row for the current column
            vert_win.append(board[row][col])  # Collect the pieces in the column  
        del vert_win[0]
        # Now check if all items in vert_win are the same
        if all(spot.strip() == "X" for spot in vert_win):  # Check for 'X'
            print(f"{player} wins vertically!")
            return True
        elif all(spot.strip() == "O" for spot in vert_win):  # Check for 'O'
            print(f"{player} wins vertically!")
            return True

    return False  # No vertical win found


board_list = create_board(board_size=BOARD_SIZE)  


while True:
    player_one = input("Would you like to be (X)'s or (O)'s?: ").upper()
    if player_one in playable_pieces:
        break
    else:
        print("Invalid choice. Please enter 'X' or 'O'.")

if player_one == 'X':
    player_two = 'O'
else:
    player_two = 'X'

is_legal = legal_move(user_piece=player_one, user_row = user_row, user_col = user_col, board=board_list)
if is_legal: 
    place_piece(user_piece=player_one, user_row="3", user_col="a", board=board_list)
    place_piece(user_piece=player_two, user_row="3", user_col="b", board=board_list)
    place_piece(user_piece=player_two, user_row="1", user_col="B", board=board_list)
    place_piece(user_piece=player_two, user_row="2", user_col="B", board=board_list)
    game_state(board = board_list, player=player_one)
draw_board(board=board_list)

