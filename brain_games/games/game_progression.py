from random import randint

MSG_RULES = 'What number is missing in the progression?'
MIN_RAND_NUM_CONST = 0
MAX_RAND_NUM_CONST = 9
MIN_RAND_NUM_START = 1
MAX_RAND_NUM_START = 99

def get_progression(max_num_items: int = 5) -> tuple:
    """
    Returns tuple with sequences (lists) and list with missed items.
    """

    d_const = randint(MIN_RAND_NUM_CONST, MAX_RAND_NUM_CONST)
    missed_index = randint(0, max_num_items - 1)
    start = randint(MIN_RAND_NUM_START, MAX_RAND_NUM_START)
    seq = []
    for _ in range(max_num_items):
        start = start + d_const
        seq.append(str(start))
    right_answer = seq[missed_index]
    seq[missed_index] = '..'
    question = ' '.join(seq)
    return question, right_answer


def get_quiz():
    return get_progression()
