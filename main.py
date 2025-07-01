from string import ascii_uppercase
import os



BOARD_SIZE = 3
playable_pieces = ["X", "O"]


# Game Board
def create_board(board_size):
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
            if (
                len(row) == 0
            ):  # if start of row, insert index + 1 (to not start at zero), along with a space for better visual
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
    string = ""
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
    if row < 0 or row >= len(board) or col_string not in board[0]:  # change
        print(
            "Your move is out of the playable bounds. Please input a valid placement."
        )
        return False

    col = board[0].index(col_string)

    if board[row][col] == " O " or board[row][col] == " X ":
        user_piece = " " + user_piece + " "
        if board[row][col] == user_piece:
            print("You already have a piece there.\n")
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
    symbol = " " + player.upper() + " "
    for row in board[1:]:  # Skip the letter row at index 0
        # Check only the cells, not the spacers (index 1, 3, 5...)
        player_cells = [row[i] for i in range(1, len(row), 2)]
        if all(cell == symbol for cell in player_cells):
            os.system("cls||clear")
            draw_board(board)
            print(f"{player} has won horizontally!")
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
            os.system("cls||clear")
            print(f"{player} wins vertically!")
            draw_board(board)
            return True
        elif all(spot.strip() == "O" for spot in vert_win):  # Check for 'O'
            os.system("cls||clear")
            draw_board(board)
            print(f"{player} wins vertically!")
            return True

    return False  # No vertical win found


def tic_tac_toe():
    board_list = create_board(board_size=BOARD_SIZE)
    letters_on_board = [letter.strip(" ") for letter in board_list[0] if letter.strip(" ") in ascii_uppercase and letter.strip() != ""]
    initialize_game = input("Would you like to play Tic Tac Toe? (Y)es, (N)o: ").upper()
    os.system("cls||clear")

    if initialize_game.startswith("Y"):
        draw_board(board=board_list)
        initialize_game = True
    else:
        initialize_game = False

    while initialize_game:
        turns_in_game = 0

        while True:
            player_one = input("Would you like to be (X)'s or (O)'s?: ").upper()
            if player_one in playable_pieces:
                break
            else:
                print("Invalid choice. Please enter 'X' or 'O'.")

        if player_one == "X":
            player_two = "O"
        else:
            player_two = "X"

        for turn in range(BOARD_SIZE * BOARD_SIZE):
            if turns_in_game == 0:
                player = player_one
            if turns_in_game % 2 == 0:
                player = player_one
            else:
                player = player_two
            while True:
                col = input(
                    f"player '{player}', what column would you like to place your piece in?: "
                ).upper()

                if col in letters_on_board:
                    row = input("what row would you like to choose?: ").upper()
                    if len(row) == 1:
                                        
                        is_legal = legal_move(
                            user_piece=player, user_row=row, user_col=col, board=board_list
                        )
                        break
                else:
                    print(f"{col} is not a valid column. Please choose again.")
            if is_legal:
                place_piece(
                    user_piece=player, user_row=row, user_col=col, board=board_list
                )
                game_over = game_state(board=board_list, player=player)
                if game_over:
                    
                    break

            turns_in_game += 1
            draw_board(board=board_list)
            if turns_in_game == BOARD_SIZE * BOARD_SIZE:
                print("No winner!")
                break
        break
    tic_tac_toe()


tic_tac_toe()
