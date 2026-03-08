from dice import Die
from player import Player
from board import Board

class LudoGame:
    def __init__(self, n_players, colors: list):
        self.players = [Player(i, color) for i in range(n_players) for color in colors]
        self.board = Board()
        self.die = Die()

    def run_game(self):
        self.take_turn()
        if self.check_win_condition():
            self.display_winner()

    def take_turn(self, player, token):
        die_roll = self.die.roll_die()
        # curr_player = self.decide_player()
        # token = self.curr_player.decide_token()
        print(f"Turn by Player {player.index} {player.color} Token {token.index}")
        self.board.move_token(token, die_roll)
        self.check_game_constraints(token)

        self.display_game_state()

    def decide_player(self):
        # rotate turn amongst players
        # grant one extra turn for 6 on die
        pass
    
    def check_game_constraints(self, token):
        pass

    def display_game_state(self):
        pass

    def check_win_condition(self):
        pass

    def display_winner(self):
        pass
    
if __name__ == "__main__":
    colors = ["RED", "BLUE", "GREEN", "YELLOW"]
    lg = LudoGame(n_players=4, colors=colors)
    # lg.run_game()
    player = lg.players[0]
    token = player.tokens[3]

    for _ in range(50):
        lg.take_turn(player, token)
        print("-" * 10)