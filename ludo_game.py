from movement_handler import BasicMovement
from dice import Die
from player import Player
from board import Board

class LudoGame:
    def __init__(self, n_players, colors: list, mover_class):
        self.players = [Player(i, color) for i in range(n_players) for color in colors]
        self.board = Board()
        self.mover_class = mover_class()
        # self.board = # create board

    # def run_game(self):
        # runs this for all players, to come up with the winner
        # curr_player.play_turn_with_token(token)

        # self.display_winner()
    
    # def display_winner(self):
    #     pass

    def play_turn_with_token(self, player, token):
        print(f"Turn by Player {player.color}, id {player.index}")
        die_roll = Die.roll_die()
        # token = player.tokens[token_index]
        self.mover_class.move_token(self.board, token, die_roll)

if __name__ == "__main__":
    colors = ["RED", "BLUE", "GREEN", "YELLOW"]
    lg = LudoGame(n_players=4, colors=colors, mover_class=BasicMovement)
    # lg.run_game()
    player = lg.players[0]
    token = player.tokens[3]

    for _ in range(50):
        lg.play_turn_with_token(player, token)
        print("-" * 10)