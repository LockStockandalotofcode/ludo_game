from enum import Enum, auto

class CellType(Enum):
    NORMAL_CELL = auto()
    SAFE_CELL = auto()

class Cell:
    def __init__(self, position, celltype=CellType.NORMAL_CELL):
        self.position = position
        self.celltype = celltype
        self.tokens = []

    def place_token(self, token):
        self.tokens.append(token)

    def remove_token(self, token):
        self.tokens.remove(token)
