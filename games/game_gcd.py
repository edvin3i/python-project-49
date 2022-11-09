

MSG_RULES = 'Find the greatest common divisor of given numbers.'

def start_gcd_game():
    name = welcome_user()

    questions = [get_couple_nums() for x in range(3)]
    right_answers = [get_gcd(couple) for couple in questions]
    game_cycle(name, questions, right_answers)
