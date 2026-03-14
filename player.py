from game_token import Token, TokenState
from random import randint

class Player:
    def __init__(self, index, color="RED"):
        self.index = index
        self.color = color
        self.tokens = [Token(index, self.color) for i in range(4)]

    def decide_token(self, die_roll):
        in_base = [t for t in self.tokens if t.state == TokenState.IN_BASE]
        on_track = [t for t in self.tokens if t.state == TokenState.ON_TRACK]

        if die_roll == 6 and in_base:
            return in_base[0]
        
        if on_track:
            return on_track[0]
        
        return None