from string import ascii_uppercase
BOARD_SIZE = 3

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



# Refactor this to seperate functions to keep it more readable
#also, include this genius check for horizontal to shorten the code by 20 lines:     
# for row in board:
    #if all(piece.strip() == player for piece in row):
        #return True
    #return False
def game_state(board, player_one, player_two):
    """A Function that checks if there is a win via horizontal, vertical, or diagonal wins"""
    row_win = []
    vertical_win = []

    for row in board:

        # check for horizontal wins
        for piece in row:
            if piece.strip() == player_one:
                row_win.append(
                    piece.strip()
                )  # strip white space from piece to equal player input
            elif piece.strip() == player_two:
                row_win.append(
                    piece.strip()
                )  # strip white space from piece to equal player input
        if len(row_win) == len(row) // 2:
            if row_win.count(player_one) == len(row) // 2:
                print(f"TESTING: {player_one} wins horizontally!")
                return True
            elif row_win.count(player_two) == len(row) // 2:
                print(f"TESTING: {player_two} wins horizontally!")
                return True

        
        row_win = []
        
        # Check for vertical wins
        # if row != []:


    return False





board_list = create_board(board_size=BOARD_SIZE)  
user_piece = 'X'
user_row = "3"
user_col = "B"

playable_pieces = ['X', 'O']

while True:
    user_one_piece = input("Would you like to be (X)'s or (O)'s?: ").upper()
    if user_one_piece in playable_pieces:
        break
    else:
        print("Invalid choice. Please enter 'X' or 'O'.")

if user_one_piece == 'X':
    user_two_piece = 'O'
else:
    user_two_piece = 'X'

is_legal = legal_move(user_piece=user_one_piece, user_row = user_row, user_col = user_col, board=board_list)
if is_legal: 
    place_piece(user_piece=user_one_piece, user_row="3", user_col="a", board=board_list)
    place_piece(user_piece=user_one_piece, user_row="3", user_col="b", board=board_list)
    place_piece(user_piece=user_one_piece, user_row="3", user_col="C", board=board_list)
    place_piece(user_piece=user_two_piece, user_row="2", user_col="B", board=board_list)
    game_state(board = board_list, player_one = user_one_piece, player_two = user_two_piece)
draw_board(board=board_list)



vert_win = []

target_index = 0
for spaces in range(len(board_list[0])):
    if board_list != []:
        vert_win.append(board_list[target_index])
        target_index += 1
    print(vert_win)