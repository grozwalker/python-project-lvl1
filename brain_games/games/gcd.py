import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)

    question = f'{num_1} {num_2}'
    answer = get_gcd(num_1, num_2)

    return (question, answer)


def get_gcd(num_1, num_2):
    gcd = 1
    bound = min(num_1, num_2) + 1

    for i in reversed(range(2, bound)):
        if num_1 % i == 0 and num_2 % i == 0:
            return i

    return gcd
