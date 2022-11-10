from games import common_core

MSG_RULES = 'What number is missing in the progression?'

def start_progression_game(game_core=common_core):
    name = game_core.welcome_user(MSG_RULES)

    questions, right_answers = game_core.get_progression(game_core.TRY_NUM)
    game_core.game_cycle(name, questions, right_answers)
