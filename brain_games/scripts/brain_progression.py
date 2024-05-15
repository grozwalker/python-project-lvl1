from ..games.progression import get_game_condition, get_exercise
from ..games.engine import play_game


def main():
    game_condition = get_game_condition
    exercise = get_exercise()

    play_game(exercise, game_condition)
