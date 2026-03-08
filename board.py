class Board:
    def __init__(self, board_size=52):
        self.size = board_size
        self.board = self._build_board(board_size)

    def _build_board(self, board_size):
        return [i for i in range(board_size)]