from math import gcd
from random import randint

MSG_RULES = 'Find the greatest common divisor of given numbers.'


def get_couple_nums() -> str:
    """Just returns string with two numbers separated by whitespace."""
    return f"{randint(0, 100)} {randint(0, 100)}"


def get_gcd(couple_nums: str) -> str:
    """
    Parameter - string with two numbers separated by whitespace.
    Returns greater common divider.
    """
    num1 = int(couple_nums.split()[0])
    num2 = int(couple_nums.split()[1])
    return str(gcd(num1, num2))


def get_quiz() -> tuple:
    question = get_couple_nums()
    right_answer = get_gcd(question)
    return question, right_answer
