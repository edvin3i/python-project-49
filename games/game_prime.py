

MSG_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def start_prime_game():
    name = welcome_user()

    questions = get_num_list(2, 1234, 3)
    right_answers = [is_prime(question) for question in questions]
    game_cycle(name, questions, right_answers)
