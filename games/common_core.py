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
MSG_RIGHT_ANSW = 'Correct!'
MSG_WRONG_ANSW = "'$user_answer' is wrong answer ;(. Correct answer was '$right_answer'."\
                 + "\nLet's try again, $name!"
MSG_CONGRATS = 'Congratulations, $name!'

TRY_NUM = 3


#############################################################################################
# ================================== Common funcs ========================================= #
#############################################################################################

def welcome_user(msg_rules):
    """Greets user and asks his/her name. Returns user's name."""
    print(MSG_WELCOME)
    name = prompt.string(MSG_ASK_NAME)
    print(f'Hello, {name}!')
    print(msg_rules)
    return name


def get_num_list(start, stop, count):
    """Parameters: start, stop, count.
    Returns list of random nums."""
    return [randint(start, stop) for x in range(count)]


def ask_question(question):
    """Asks question from input argument and returns user's answer."""
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def game_cycle(name, questions, right_answers):
    """Main game cycle. Receive username,
     list with questions and list with correct answers."""
    try_count = 0
    msg_wrong_answ = Template(MSG_WRONG_ANSW)
    msg_congrats = Template(MSG_CONGRATS)
    while try_count < TRY_NUM:
        user_answer = ask_question(questions[try_count]).lower()
        if right_answers[try_count] == user_answer:
            print(MSG_RIGHT_ANSW)
        else:
            msg_wrong_answ.substitute(name=name,
                                      user_answer=user_answer,
                                      right_answer=right_answers[try_count])
            return
        try_count += 1
    msg_congrats.substitute(name=name)

#############################################################################################
# ================================ Specific for games funcs =============================== #
#############################################################################################


def get_expression():
    """Returns random expression for two numbers and random action(+, -, *)."""
    return f"{randint(0, 100)} {choice('+-*')} {randint(0, 100)}"


def is_prime(num):
    """Parameter - is a number. Returns 'yes' if it prime or 'no' if not."""
    for i in range(2, num):
        if (num % i) == 0:
            return 'no'
    return 'yes'


def is_even(num):
    """Parameter - is a number. Returns 'yes' if it even and 'no' if not."""
    if num % 2:
        return 'no'
    return 'yes'


def get_couple_nums():
    """Just returns string with two numbers separated by whitespace."""
    return f"{randint(0, 100)} {randint(0, 100)}"


def get_gcd(couple_nums):
    """Parameter - string with two numbers separated by whitespace.
    Returns greater common divider."""
    num1 = int(couple_nums.split()[0])
    num2 = int(couple_nums.split()[1])
    return str(gcd(num1, num2))


def get_progression(max_num_items=5):
    """Parameter - max number of items in sequence.
    Returns tuple with 3 sequences (lists) and list with missed items."""
    result = ()
    sequences = []
    missed_items = []
    for _ in range(3):
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

