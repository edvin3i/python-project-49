from random import randint
from games.common_core import welcome_user
from games.common_core import game_cycle


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return 'no'
    return 'yes'


def start_prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    questions = [randint(2, 1234) for x in range(3)]
    right_answers = [is_prime(question) for question in questions]
    game_cycle(name, questions, right_answers)
