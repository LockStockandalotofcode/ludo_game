from token import Token, TokenState
from cell import Cell, CellType

class Board:
    def __init__(self, board_size=52):
        self.board_size = board_size
        self.board = self._create_board(board_size)

    def _create_board(self, board_size):
        board = [Cell(position=i) for i in range(board_size)]
        board = self.mark_safe_zones(board)
        return board
    
    def mark_safe_zones(self, board):
        mapping = []
        for i in mapping:
            board[i].celltype = CellType.SAFE_CELL
        return board
    
    def move_token(self, token: Token, die_roll: int):
        # move out of base onto track
        if token.state == TokenState.IN_BASE:
            if die_roll == 6:
                self.move_token_from_base(token)
                print(f"{token.index} moved from base on to track")
        # move on track
        else:
            self.move_token_on_track(token, die_roll)
            print(f"{token.state} New position of token-{token.index} is {token.position}")
        
    def move_token_from_base(self, token):
        token.state = TokenState.ON_TRACK
        token.position = 0
        cell = self.board[token.position]
        cell.place_token(token)

    def move_token_on_track(self, token, steps):
        cell = self.board[token.position]
        cell.remove_token(token)
        token.position = (token.position + steps) % self.board_size
        cell = self.board[token.position]
        cell.place_token(token)