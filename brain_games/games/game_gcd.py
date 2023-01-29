from math import gcd
from random import randint

MSG_RULES = 'Find the greatest common divisor of given numbers.'
MIN_RAND_NUM = 0
MAX_RAND_NUM = 100

def get_couple_nums() -> tuple:
    """Just returns string with two numbers separated by whitespace."""
    return randint(MIN_RAND_NUM, MAX_RAND_NUM), randint(MIN_RAND_NUM, MAX_RAND_NUM)


def get_gcd(num1: int, num2: int) -> str:
    """
    Parameter - string with two numbers separated by whitespace.
    Returns greater common divider.
    """
    return str(gcd(num1, num2))


def get_quiz() -> tuple:
    num1, num2 = get_couple_nums()
    question = f'{num1}, {num2}'
    right_answer = get_gcd(num1, num2)
    return question, right_answer
