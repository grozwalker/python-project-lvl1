import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_game_data():
    question = random.randint(0, 100)
    answer = is_even(question)

    return (question, answer)
