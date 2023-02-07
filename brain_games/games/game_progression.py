from random import randint
from brain_games.utils import get_answer

MSG_RULES = 'What number is missing in the progression?'
MIN_RAND_NUM_CONST = 0
MAX_RAND_NUM_CONST = 9
MIN_RAND_NUM_START = 1
MAX_RAND_NUM_START = 99
MAX_NUM_ITEMS = 5

def get_progression() -> tuple:
    """
    Returns tuple with sequences (lists) and list with missed items.
    """

    d_const = randint(MIN_RAND_NUM_CONST, MAX_RAND_NUM_CONST)
    start = randint(MIN_RAND_NUM_START, MAX_RAND_NUM_START)
    seq = []
    for _ in range(MAX_NUM_ITEMS):
        start = start + d_const
        seq.append(str(start))
    return seq
    

def get_question(progr):
    missed_index = randint(0, len(progr) - 1)
    right_answer = progr[missed_index]
    progr[missed_index] = '..'
    question = ' '.join(progr)
    return question, get_answer(right_answer)


def get_quiz():
    return get_question(get_progression())
