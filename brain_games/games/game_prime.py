from random import randint
from brain_games.utils import get_answer

MSG_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM = 2
MAX_NUM = 1234


def is_prime(num: int) -> str:
    """
    Parameter - is a number.
    Returns 'yes' if it prime or 'no' if not.
    """
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def get_quiz() -> tuple:
    question = randint(MIN_NUM, MAX_NUM)
    right_answer = get_answer(is_prime(question))
    return question, right_answer
