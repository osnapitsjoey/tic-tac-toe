
from gameboard import GameBoard

game_board: GameBoard = GameBoard()       # 👈 this creates an INSTANCE of the class

# when game_start:
#     draw_board
#     ask_user = input(play against you or ai?)
#     if ask_user is ai:
#       initiate ai
#     else:
#       play with two players
#     if check_winner():
#        show winner and show winning board or show draw
#     else:
#       ask player 1 for move
#           if move_is_legal:
#               ask/have ai move player 2
#                   if move_is_legal:
#                       update board
#     next turn

# board_size = 5
# board = []
# for num in range(board_size):
#     board.append(" ")
# board = [board] * board_size
# print(board)

game_board.draw_board()