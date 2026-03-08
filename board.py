from token import Token, TokenState
from cell import Cell

class Board:
    def __init__(self, board_size=52):
        self.size = board_size
        self.board = self._build_board(board_size)

    def _build_board(self, board_size):
        board = [Cell.create_cell(i) for i in range(board_size)]
        # safe_zones = []
        # for i in safe_zones:
        #     board[i].celltype = CellType.SAFE_CELL
        return board
    
    def move_token(self, token: Token, die_roll: int):
        # move out of base onto track
        if token.state == TokenState.IN_BASE:
            if die_roll == 6:
                token.state = TokenState.ON_TRACK
                token.position = 0

                print(f"{token.index} moved on to track")
        # move on track
        else:
            token.position = (token.position + die_roll) % self.size
            # if token.position <= 
            print(f"{token.state} New position of token-{token.index} is {token.position}")