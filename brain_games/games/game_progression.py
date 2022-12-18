from random import randint

MSG_RULES = 'What number is missing in the progression?'

def get_progression(max_num_items: int = 5) -> tuple:
    """
    Parameters - max number of items in sequence (default = 5),
    number of items (sequences) in returned tuple
    Returns tuple with sequences (lists) and list with missed items.
    """

    d_const = randint(1, 9)
    missed_index = randint(0, max_num_items - 1)
    start = randint(1, 99)
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
