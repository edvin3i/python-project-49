from random import randint
from brain_games.utils import get_answer

MSG_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RND_NUM = 1
MAX_RND_NUM = 100


def is_even(num: int) -> bool:
    """
    Parameter - is a number.
    Returns 'yes' if it even and 'no' if not.
    """
    return num % 2 == 0


def get_quiz():
    question = randint(MIN_RND_NUM, MAX_RND_NUM)
    right_answer = get_answer(is_even(question))
    return question, right_answer
