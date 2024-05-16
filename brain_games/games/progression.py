import random


def get_exercise():
    return 'What number is missing in the progression?'


def get_game_condition():
    PROGRESSION_LENGHT = 10

    first_elem = random.randint(0, 50)
    step = random.randint(1, 10)
    hided_elem = random.randint(1, 10)

    cur = first_elem
    progression = [str(first_elem)]

    for i in range(1, PROGRESSION_LENGHT):
        cur += step

        if i == hided_elem:
            progression.append('..')
            answer = cur
        else:
            progression.append(str(cur))

    question = ' '.join(progression)

    return (question, answer)
