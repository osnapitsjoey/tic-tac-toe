
#board_size = 3
# def create_board(size):
#     board = []
#     for i in range(size):
#         board.append([" ", " ", " "])
#     return board

# print(create_board(size=board_size))


# def check_vertical_win(board):
#     index = 0
#     forward_diag_win = []
#     backward_diag_win = []
#     for row in board:
#         forward_diag_win.append(row[index])
#         index += 1
#     index = 0
#     for row in reversed(board):
#         backward_diag_win.append(row[index])
#         index += 1

#     if forward_diag_win.count("X") == len(board) or backward_diag_win.count("X") == len(board):
#         return "X wins"
#     elif forward_diag_win.count("O") == len(board) or backward_diag_win.count("O") == len(board):
#         return "O wins"
#     else:
#         return None

# def check_vertical_win(board):
#     diag_win = []
#     backward_diag_win = []
#     for index in range(len(board)):
#         diag_win.append(board[index][index]) # Check for forward Diagonal win
#         backward_diag_win.append(board[index][len(board) -1 -index])  # Check for forward Diagonal

#     if diag_win.count("X") == len(board) or backward_diag_win.count("X") == len(
#         board
#     ):
#         return "X wins"
#     elif diag_win.count("O") == len(board) or backward_diag_win.count(
#         "O"
#     ) == len(board):
#         return "O wins"
#     else:
#         return None

x_win = [["X", "O", " "], ["X", " ", "O"], ["X", " ", " "]]
o_win = [[" ", "O", "X"], [" ", "O", " "], ["X", "O", " "]]
no_win = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
board = 3
def check_vertical_win(board):
    for col in range(len(board[0])):  # Loop over each column
        vert_win = []  # Reset the vertical win tracker for this column
        for row in range(len(board)):  # Loop through each row for the current column
            vert_win.append(board[row][col])  # Collect the pieces in the column

        # Now check if all items in vert_win are the same
        if all(spot.strip() == "X" for spot in vert_win):  # Check for 'X'
            print("X wins vertically!")
            return True
        elif all(spot.strip() == "O" for spot in vert_win):  # Check for 'O'
            print("O wins vertically!")
            return True

    return False  # No vertical win found


#print(check_vertical_win(x_win))
print(check_vertical_win(o_win))
#print(check_vertical_win(no_win))