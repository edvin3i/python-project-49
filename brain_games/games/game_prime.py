from random import randint

MSG_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM = 2
MAX_NUM = 1234
COUNT_NUM = 3


def get_num_list(start: int,
                 stop: int,
                 count: int) -> list:
    """
    Parameters: start, stop, count.
    Returns list of random nums.
    """
    return [randint(start, stop) for x in range(count)]


def is_prime(num: int) -> str:
    """
    Parameter - is a number.
    Returns 'yes' if it prime or 'no' if not.
    """
    for i in range(2, num):
        if (num % i) == 0:
            return 'no'
    return 'yes'


def get_quiz():
  question = get_num_list(MIN_NUM, MAX_NUM, COUNT_NUM)
  right_answer = is_prime(question)
  return question, right_answer
