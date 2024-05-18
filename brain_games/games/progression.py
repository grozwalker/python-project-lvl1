import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10


def get_game_data():
    first_elem = random.randint(0, 50)
    step = random.randint(1, 10)
    hided_elem = random.randint(0, 9)

    progression = []
    current = first_elem

    for _ in range(PROGRESSION_LENGHT):
        progression.append(str(current))
        current += step

    answer = progression[hided_elem]
    progression[hided_elem] = '..'

    question = ' '.join(progression)

    return (question, answer)
