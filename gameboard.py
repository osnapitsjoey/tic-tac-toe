from string import ascii_uppercase


board_size = 5
letter_grid = []

board = []
for _ in range(board_size):
    row = []
    for col in range(board_size * 2 - 1): # doubles the size of grid to accommodate spacers, and stops one short of adding a third spacer
        if len(row) == 0:
            row.append(_ + 1)
        if col % 2 == 0: # checks if dividing the current index of col is zero, if true places a '-', if false, adds a '|'
            row.append(" - ") # playable space
        else:
            row.append(" | ") # spacer
    board.append(row) # builds the row up until it finishes the for loops, starting the row list over again

for i in range(board_size):
    letter_grid.append(" ")
    letter_grid.append(ascii_uppercase[i])
    
board.insert(0, letter_grid)

print (board)

print(len(board[0]))