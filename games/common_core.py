import prompt


def welcome_user():
    """Greets user and asks his/her name. Returns user's name"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(question):
    """Asks question from input argument and returns user's answer"""
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def game_cycle(name, questions, right_answers):
    """Main game cycle. Recive username,
     list with questions and list with correct answers"""
    try_num = 0
    while try_num < 3:
        user_answer = ask_question(questions[try_num]).lower()
        if right_answers[try_num] == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{right_answers[try_num]}'.")
            print(f"Let's try again, {name}!")
            return
        try_num += 1
    print(f'Congratulations, {name}!')
