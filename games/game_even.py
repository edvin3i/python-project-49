

MSG_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def start_even_game():
    name = welcome_user()

    questions = [randint(1, 100) for x in range(3)]
    right_answers = [is_even(num) for num in questions]
    game_cycle(name, questions, right_answers)
