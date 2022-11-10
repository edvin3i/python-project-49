"""
Main module (engine) for Brain Games.
Module represents some functions needed for arithmetic games.
"""

from math import gcd
from random import randint
from random import choice
from string import Template
import prompt


#############################################################################################
# ==================================== Constants ========================================== #
#############################################################################################

MSG_WELCOME = "Welcome to the Brain Games!"
MSG_ASK_NAME = 'May I have your name? '
MSG_HELLO = 'Hello, $name!'
MSG_RIGHT_ANSW = 'Correct!'
MSG_WRONG_ANSW = "'$user_answer' is wrong answer ;(. Correct answer was '$right_answer'."\
                 + "\nLet's try again, $name!"
MSG_CONGRATS = 'Congratulations, $name!'

TRY_NUM = 3


#############################################################################################
# ================================== Common funcs ========================================= #
#############################################################################################

def welcome_user(msg_rules: str):
    """Greets user and asks his/her name. Returns user's name."""
    msg_hello = Template(MSG_HELLO)
    print(MSG_WELCOME)
    name = prompt.string(MSG_ASK_NAME)
    print(msg_hello.substitute(name=name))
    print(msg_rules)
    return name


def get_num_list(start: int,
                 stop: int,
                 count: int):
    """
    Parameters: start, stop, count.
    Returns list of random nums.
    """
    return [randint(start, stop) for x in range(count)]


def ask_question(question: str):
    """Asks question from input argument and returns user's answer."""
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def game_cycle(name: str,
               questions: list,
               right_answers: list):
    """
    Main game cycle. Receive username,
    list with questions and list with correct answers.
    """
    try_count = 0
    msg_wrong_answ = Template(MSG_WRONG_ANSW)
    msg_congrats = Template(MSG_CONGRATS)
    while try_count < TRY_NUM:
        user_answer = ask_question(questions[try_count]).lower()
        if right_answers[try_count] == user_answer:
            print(MSG_RIGHT_ANSW)
        else:
            print(msg_wrong_answ.substitute(name=name,
                                      user_answer=user_answer,
                                      right_answer=right_answers[try_count]))
            return
        try_count += 1
    print(msg_congrats.substitute(name=name))

#############################################################################################
# ================================ Games specific funcs =============================== #
#############################################################################################


def get_expression():
    """Returns random expression for two numbers and random action(+, -, *)."""
    return f"{randint(0, 100)} {choice('+-*')} {randint(0, 100)}"


def is_prime(num: int):
    """
    Parameter - is a number.
    Returns 'yes' if it prime or 'no' if not.
    """
    for i in range(2, num):
        if (num % i) == 0:
            return 'no'
    return 'yes'


def is_even(num: int):
    """
    Parameter - is a number.
    Returns 'yes' if it even and 'no' if not.
    """
    if num % 2:
        return 'no'
    return 'yes'


def get_couple_nums():
    """Just returns string with two numbers separated by whitespace."""
    return f"{randint(0, 100)} {randint(0, 100)}"


def get_gcd(couple_nums: str):
    """
    Parameter - string with two numbers separated by whitespace.
    Returns greater common divider.
    """
    num1 = int(couple_nums.split()[0])
    num2 = int(couple_nums.split()[1])
    return str(gcd(num1, num2))


def get_progression(items_num: int,
                    max_num_items: int = 5):
    """
    Parameters - max number of items in sequence (default = 5),
    number of items (sequences) in returned tuple
    Returns tuple with sequences (lists) and list with missed items.
    """
    result = ()
    sequences = []
    missed_items = []
    for _ in range(items_num):
        d_const = randint(1, 9)
        missed_index = randint(0, max_num_items - 1)
        start = randint(1, 99)
        seq = []
        for _ in range(max_num_items):
            start = start + d_const
            seq.append(str(start))
        missed_items.append(seq[missed_index])
        seq[missed_index] = '..'
        sequences.append(' '.join(seq))
    result += (sequences,)
    result += (missed_items,)
    return result

#############################################################################################
