from dice import Die
from player import Player
from board import Board

class LudoGame:
    def __init__(self, n_players, colors: list):
        self.players = [Player(i, color) for i in range(n_players) for color in colors]
        self.board = Board()
        self.die = Die()

    def play_turn_with_token(self, player, token):
        print(f"Turn by Player {player.index} {player.color}")
        die_roll = self.die.roll_die()
        # token = player.tokens[token_index]
        self.board.move_token(token, die_roll)

     # def run_game(self):
        # runs this for all players, to come up with the winner
        # curr_player.play_turn_with_token(token)

        # self.display_winner()
    
    # def display_winner(self):
    #     pass
    
if __name__ == "__main__":
    colors = ["RED", "BLUE", "GREEN", "YELLOW"]
    lg = LudoGame(n_players=4, colors=colors)
    # lg.run_game()
    player = lg.players[0]
    token = player.tokens[3]

    for _ in range(50):
        lg.play_turn_with_token(player, token)
        print("-" * 10)