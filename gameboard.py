
class GameBoard:

    def __init__(self):
        self.board_size: int = 3
        self.board: list[list[str]] = self.create_board()
        
    
    
    def create_board(self) -> list[list[str]]:
        board: list[list[str]] = []
        for _ in range(self.board_size):
            row: list[str] = [" " for _ in range(self.board_size)]
            board.append(row)
        return board

    def draw_board(self):
        """method to draw the board onto the screen"""
        for row in self.board:
            print('|'.join(row))
            print('- ' * (self.board_size))

