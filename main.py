from string import ascii_uppercase
BOARD_SIZE = 5

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

def draw_board(board) -> str:
    """Displays the game board as characters aesthetically"""
    string = ''
    for row in board:
        for char in row:
            string += char
        print(string)
        string = ""
        

# Game Logic

def legal_move(user_row, user_col, board, user_piece):
    row = int(user_row)
    col = board[0].index("  " + user_col.upper() + "  ") # Confirm user_col matches the format in board[0]
    if row < 0 or row >= len(board) or col not in board[0]:
        print('Your move is out of the playable bounds. Please input a valid placement.')
        return False
    elif board[row][col] == ' O ' or board[row][col] == ' X ':
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


board_list = create_board(BOARD_SIZE)
print(board_list)
print(board_list[1].index("1 "))

user_piece = 'X'
user_row = "4"
user_col = "A"
#legal_move(user_row, user_col, board_list, user_piece)
place_piece(user_piece, user_row, user_col, board_list)
draw_board(board_list)