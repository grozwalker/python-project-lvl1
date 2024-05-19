import prompt


NUMBER_OF_ROUND = 3


def run(game):

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    print(game.DESCRIPTION)

    for _ in range(NUMBER_OF_ROUND):
        question, expected_answer = game.get_game_data()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == str(expected_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
