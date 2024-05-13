import prompt


def play_game(exercise, game_condition):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    print(exercise)

    NUM_ATTEMPTS = 3

    for _ in range(NUM_ATTEMPTS):
        question, correct_answer = game_condition()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
