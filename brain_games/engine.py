import prompt


def play_game(game_goal, game_data):
    ATTEMPTS = 3

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    print(game_goal)

    for _ in range(ATTEMPTS):
        question, correct_answer = game_data()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
