"""
Main module (engine) for Brain Games.
Module represents some functions needed for arithmetic games.
"""

from string import Template
import prompt


MSG_WELCOME = "Welcome to the Brain Games!"
MSG_ASK_NAME = 'May I have your name? '
MSG_HELLO = 'Hello, $name!'
MSG_RIGHT_ANSW = 'Correct!'
MSG_WRONG_ANSW = "'$user_answer' is wrong answer ;(." \
                 + "Correct answer was '$right_answer'." \
                 + "\nLet's try again, $name!"
MSG_CONGRATS = 'Congratulations, $name!'

TRY_NUM = 3


def welcome_user(msg_rules: str) -> str:
    """Greets user and asks his/her name. Returns user's name."""
    msg_hello = Template(MSG_HELLO)
    print(MSG_WELCOME)
    name = prompt.string(MSG_ASK_NAME)
    print(msg_hello.substitute(name=name))
    print(msg_rules)
    return name


def ask_question(question: str) -> str:
    """Asks question from input argument and returns user's answer."""
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def run_game(game) -> None:
    """
    Main game cycle. Receive username,
    list with questions and list with correct answers.
    """
    try_count = TRY_NUM
    name = welcome_user(game.MSG_RULES)

    msg_wrong_answ = Template(MSG_WRONG_ANSW)
    msg_congrats = Template(MSG_CONGRATS)
    while try_count:
        question, right_answer = game.get_quiz()
        user_answer = ask_question(question).lower()
        if right_answer != user_answer:
            print(
                msg_wrong_answ.substitute(name=name,
                                          user_answer=user_answer,
                                          right_answer=right_answer))
            return
        try_count -= 1
        print(MSG_RIGHT_ANSW)
    print(msg_congrats.substitute(name=name))
