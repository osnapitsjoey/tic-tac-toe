
# board_size = 3
# def create_board(size):
#     board = []
#     for i in range(size):
#         board.append([" ", " ", " "])
#     return board

# print(create_board(size=board_size))

x_win = [["X", " ", "O"], [" ", "X", " "], ["O", " ", "X"]]
o_win = [["X", "O", "O"], [" ", "O", " "], ["O", " ", "X"]]
no_win = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# def check_diagonal_win(board):
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

def check_diagonal_win(board):
    diag_win = []
    backward_diag_win = []
    for index in range(len(board)):
        diag_win.append(board[index][index]) # Check for forward Diagonal win
        backward_diag_win.append(board[index][len(board) -1 -index])  # Check for forward Diagonal

    if diag_win.count("X") == len(board) or backward_diag_win.count("X") == len(
        board
    ):
        return "X wins"
    elif diag_win.count("O") == len(board) or backward_diag_win.count(
        "O"
    ) == len(board):
        return "O wins"
    else:
        return None


print(check_diagonal_win(x_win))
print(check_diagonal_win(o_win))
print(check_diagonal_win(no_win))