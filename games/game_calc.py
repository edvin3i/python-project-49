from games import common_core

MSG_RULES = 'What is the result of the expression?'

def start_calc_game():
    name = welcome_user()

    questions = [get_expression() for x in range(3)]
    right_answers = [str(eval(expression)) for expression in questions]
    game_cycle(name, questions, right_answers)
