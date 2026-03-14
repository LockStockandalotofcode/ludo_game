import pytest
from unittest.mock import patch
from ludo_game import LudoGame
from game_token import TokenState

@pytest.fixture
def game():
    return LudoGame(n_players=4, colors = ["RED", "BLUE", "GREEN", "YELLOW"])

def test_initialisation(game):
    assert len(game.players) == 4
    assert game.players[0].color == "RED"

def test_move_out_of_base_on_six(game):
    player = game.players[0]
    token = player.tokens[0]

    game.board.move_token(token, die_roll=6)

    assert token.state == TokenState.ON_TRACK
    assert token.position == 0
    assert token in game.board.board_cells[0].tokens

def test_no_move_on_less_than_6(game):
    player = game.players[0]
    token = player.tokens[0]

    game.board.move_token(token, die_roll=4)

    assert token.state == TokenState.IN_BASE
    assert token.position == -1

# def test_player_rotation()

# def test_extra_turn_on_six()


