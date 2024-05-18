import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_game_data():
    question = random.randint(0, 100)
    answer = 'yes' if is_even(question) else 'no'

    return (question, answer)
