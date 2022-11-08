from random import choice
from random import randint
from games.common_core import welcome_user
from games.common_core import game_cycle


def get_expression():
    """Returns random expression for two numbers and random action(+, -, *)"""
    return f"{randint(0, 100)} {choice('+-*')} {randint(0, 100)}"


def start_calc_game():
    name = welcome_user()
    print("What is the result of the expression?")

    questions = [get_expression() for x in range(3)]
    right_answers = [str(eval(expression)) for expression in questions]
    game_cycle(name, questions, right_answers)
