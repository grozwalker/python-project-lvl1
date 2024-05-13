import random


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_exercise():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_condition():
    number = random.randint(0, 100)
    answer = is_even(number)

    return (number, answer)
