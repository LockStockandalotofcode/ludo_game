from dice import Die
from player import Player
from game_token import Token, TokenState
from board import Board

class LudoGame:
    def __init__(self, n_players, colors: list):
        self.players = [Player(i, colors[i]) for i in range(n_players)]
        self.n_players = n_players
        self.current_player_index = 0
        self.board = Board()
        self.die = Die()

    def run_game(self):
        while not self.check_win_condition():
            # for all players
            self.take_turn()
        # if self.check_win_condition():
        self.display_winner()

    def take_turn(self):
        die_roll = self.die.roll_die()
        player = self.decide_player(die_roll)
        token = player.decide_token()
        print(f"Turn by Player {player.index} {player.color}")
        if token is None:
            print(f"all tokens in base, turn skipped")
            return
        print(f"Token {token.index}")
        self.board.move_token(token, die_roll)
        self.display_game_state()

    def decide_player(self, die_roll):
        current_player = self.players[self.current_player_index]
        if die_roll != 6:
            self.current_player_index = (self.current_player_index + 1) % self.n_players
        return current_player

    def display_game_state(self):
        for player in self.players:
            print(f"Player {player.index} {player.color}") 
            for token in player.tokens:
                print(f"Token {token.index} position = {token.position}")

    def check_win_condition(self):
        for player in self.players:
            if all(t.state == TokenState.FINISHED for t in player.tokens):
                return True
        return False

    def display_winner(self):
        for player in self.players:
            for token in player.tokens:
                if token.state == TokenState.FINISHED:
                    continue
                else:
                    break
            print(f"Player {player.index} {player.color}")
    