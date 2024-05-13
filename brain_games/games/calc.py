import random


def get_answer(num_1, num_2, operator):
    match operator:
        case '-':
            result = num_1 - num_2
        case '+':
            result = num_1 + num_2
        case '*':
            result = num_1 * num_2

    return result


def get_exercise():
    return 'What is the result of the expression?'


def get_game_condition():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    operators = ['-', '+', '*']
    operator = random.choice(operators)

    question = f'{num_1} {operator} {num_2}'
    answer = get_answer(num_1, num_2, operator)

    return (question, answer)
