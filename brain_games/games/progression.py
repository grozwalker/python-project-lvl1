import random


def get_game_goal():
    return 'What number is missing in the progression?'


def get_game_data():
    PROGRESSION_LENGHT = 10

    first_elem = random.randint(0, 50)
    step = random.randint(1, 10)
    hided_elem = random.randint(0, 9)

    current = first_elem
    progression = []

    for _ in range(PROGRESSION_LENGHT):
        progression.append(str(current))
        current += step

        # if i == hided_elem:
        #     progression.append('..')
        #     answer = cur
        # else:
        #     progression.append(str(cur))

    answer = progression[hided_elem]
    progression[hided_elem] = '..'

    question = ' '.join(progression)

    return (question, answer)
