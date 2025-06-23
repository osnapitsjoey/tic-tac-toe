
BOARD_SIZE = 3


def create_board(board_size):

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
                row.append("-") # playable space
            else:
                row.append("|") # spacer
        board.append(row) # builds the row up until it finishes the for loops, starting the row list over again

    return board


board_coords = create_board(BOARD_SIZE)
print(board_coords)