import random


def get_game_goal():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    primes = (
        2, 3, 5, 7, 11, 13, 17,
        19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97
    )

    return num in primes


def get_game_data():

    question = random.randint(1, 100)

    answer = 'yes' if is_prime(question) else 'no'

    return (question, answer)
