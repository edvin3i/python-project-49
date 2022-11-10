from games import common_core

MSG_RULES = 'Find the greatest common divisor of given numbers.'


def start_gcd_game(game_core=common_core):
    name = game_core.welcome_user(MSG_RULES)
    questions = [game_core.get_couple_nums() for x in range(game_core.TRY_NUM)]
    right_answers = [game_core.get_gcd(couple) for couple in questions]
    game_core.game_cycle(name, questions, right_answers)
