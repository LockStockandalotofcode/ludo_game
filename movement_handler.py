from abc import ABC, abstractmethod
from token import Token, TokenState
from board import Board

class IMovementHandler(ABC):
    @abstractmethod
    def move_token(self, token: Token, die_roll: int):
        pass

class BasicMovement(IMovementHandler):
    def move_token(self, board: Board, token: Token, die_roll: int):
        # move out of base onto track
        if token.state == TokenState.IN_BASE:
            if die_roll == 6:
                token.state = TokenState.ON_TRACK
                token.position = 0
                print(f"{token.index} moved on to track")
        # move on track
        else:
            token.position = (token.position + die_roll) % board.size
            # if token.position <= 
            print(f"State: {token.state} New position of token-{token.index} is {token.position}")