from games import common_core

MSG_RULES = 'What is the result of the expression?'


def start_calc_game(game_core=common_core):
    name = game_core.welcome_user(MSG_RULES)
    questions = [game_core.get_expression() for _ in range(game_core.TRY_NUM)]
    right_answers = [str(eval(expression)) for expression in questions]
    game_core.game_cycle(name, questions, right_answers)
