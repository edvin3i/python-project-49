

MSG_RULES = 'What number is missing in the progression?'

def start_progression_game():
    name = welcome_user()

    questions, right_answers = get_progression()
    game_cycle(name, questions, right_answers)
