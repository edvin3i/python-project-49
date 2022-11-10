from games import common_core

MSG_RULES = 'What number is missing in the progression?'

def start_progression_game(game_core=common_core):
    name = common_core.welcome_user(MSG_RULES)

    questions, right_answers = common_core.get_progression(common_core.TRY_NUM)
    common_core.game_cycle(name, questions, right_answers)
