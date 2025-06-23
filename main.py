
BOARD_SIZE = 5

# Game Board
def create_board(board_size) -> list:

    """
    Create a tic-tac-toe board with the specified size.

    Args:
        board_size (int): The size of the board (number of rows and columns).

    Returns:
        list: A 2D list representing the game board, where each cell is initialized to "-".
    """

    board = []
    for _ in range(board_size):
        row = []
        for col in range(board_size * 2 - 1): # doubles the size of grid to accommodate spacers, and stops one short of adding a third spacer
            if col % 2 == 0: # checks if dividing the current index of col is zero, if true places a '-', if false, adds a '|'
                row.append(" - ") # playable space
            else:
                row.append(" | ") # spacer
        board.append(row) # builds the row up until it finishes the for loops, starting the row list over again

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

def legal_move(user_move, user_row, user_col, board):
    pass 

def place_piece(user_piece, user_row, user_col, board):
    # if legal_move():
    if user_col == 1:
        board[user_row - 1][0] = " " + user_piece + " "
    elif user_col % 2 == 0:
        board[user_row - 1][user_col] = " " + user_piece + " "
    else:
        board[user_row - 1][user_col + 1] = " " + user_piece + " "
    return board


board_list = create_board(BOARD_SIZE)
#draw_board(board_list)
user_piece = 'X'
user_row = 2
user_col = 5
place_piece(user_piece, user_row, user_col, board_list)
draw_board(board_list)