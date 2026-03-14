from token import Token
from random import randint

class Player:
    def __init__(self, index, color="RED"):
        self.index = index
        self.color = color
        self.tokens = [Token(index, self.color) for i in range(1, 5)]

    def decide_token(self):
        return self.tokens[randint(1, 4)]