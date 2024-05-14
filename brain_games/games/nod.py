import random


def get_exercise():
    return 'Find the greatest common divisor of given numbers.'


def get_game_condition():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)

    question = f'{num_1} {num_2}'
    answer = get_node(num_1, num_2)

    return (question, answer)


def get_node(num_1, num_2):
    nod = 1
    bound = max(num_1, num_2) // 2

    for i in range(2, bound):
        if num_1 % i == 0 and num_2 % i == 0:
            nod = i

    return nod
