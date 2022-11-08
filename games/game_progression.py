#!/usr/bin/env python3

from random import randint
from games.common_core import welcome_user
from games.common_core import game_cycle


def get_progression(max_num_items=5):
    """Parameter - max number of items in sequence. Returns tuple with 3 sequences (lists) and list with missed items"""
    result = ()
    sequences = []
    missed_items = []
    for i in range(3):
        d_const = randint(1, 9)
        missed_index = randint(0, max_num_items - 1)
        start = randint(1, 99)
        seq = []
        for j in range(max_num_items):
            start = start + d_const
            seq.append(str(start))
        missed_items.append(seq[missed_index])
        seq[missed_index] = '..'
        sequences.append(' '.join(seq))
    result += (sequences,)
    result += (missed_items,)
    return result


def start_progression_game():
    name = welcome_user()
    print('What number is missing in the progression?')
    questions, right_answers = get_progression()
    game_cycle(name, questions, right_answers)
