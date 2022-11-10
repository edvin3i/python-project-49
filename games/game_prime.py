from games import common_core

MSG_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM = 2
MAX_NUM = 1234
COUNT_NUM = 3


def start_prime_game(game_core=common_core):
    name = game_core.welcome_user(MSG_RULES)
    questions = common_core.get_num_list(MIN_NUM, MAX_NUM, COUNT_NUM)
    right_answers = [common_core.is_prime(question) for question in questions]
    common_core.game_cycle(name, questions, right_answers)
