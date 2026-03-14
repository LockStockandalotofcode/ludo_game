from enum import Enum, auto

class TokenState(Enum):
    IN_BASE = auto()
    ON_TRACK = auto()
    FINISHED = auto()

class Token:
    def __init__(self, index, color, position=-1):
        self.index = index
        self.color = color
        self.position = position
        self.state = TokenState.IN_BASE