from token import Token

class Player:
    def __init__(self, index, color="RED"):
        self.index = index
        self.color = color
        self.tokens = [Token(index, self.color) for i in range(4)]