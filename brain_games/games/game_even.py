from random import randint

MSG_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RND_NUM = 1
MAX_RND_NUM = 100


def is_even(num: int) -> str:
    """
    Parameter - is a number.
    Returns 'yes' if it even and 'no' if not.
    """
    if num % 2:
        return 'no'
    return 'yes'

def get_quiz():
  question = randint(MIN_RND_NUM, MAX_RND_NUM)
  right_answer = is_even(question)
  return question, right_answer
