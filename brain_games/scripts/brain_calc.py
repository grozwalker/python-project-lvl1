from ..games.calc import get_game_data, get_game_goal
from ..engine import play_game


def main():
    game_data = get_game_data
    game_goal = get_game_goal()

    play_game(game_goal, game_data)
