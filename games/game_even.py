from games import common_core
from random import randint

MSG_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RND_NUM = 1
MAX_RND_NUM = 100

def start_even_game(game_core=common_core):
    name = game_core.welcome_user(MSG_RULES)

    questions = [randint(MIN_RND_NUM, MAX_RND_NUM) for x in range(game_core.TRY_NUM)]
    right_answers = [game_core.is_even(num) for num in questions]
    game_core.game_cycle(name, questions, right_answers)
