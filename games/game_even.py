from random import randint
from games.common_core import welcome_user
from games.common_core import game_cycle


def is_even(num):
    if num % 2:
        return 'no'
    return 'yes'


def start_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    questions = [randint(1, 100) for x in range(3)]
    right_answers = [is_even(num) for num in questions]
    game_cycle(name, questions, right_answers)
