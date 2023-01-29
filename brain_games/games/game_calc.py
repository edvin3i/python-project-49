from random import randint, choice
import operator


MSG_RULES = 'What is the result of the expression?'
MIN_RAND_NUM = 0
MAX_RAND_NUM = 100
OPERATIONS = (
    ("+", operator.add),
    ("-", operator.sub),
    ("*", operator.mul),
)


def get_expression() -> tuple:
    """Returns random expression for two numbers and random action(+, -, *)."""
    num1 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    num2 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    operation_sym, operation_fn = choice(OPERATIONS)
    question = f"{num1} {operation_sym} {num2}"
    right_answer = str(operation_fn(num1, num2))
    return question, right_answer


def get_quiz() -> tuple:
    return get_expression()
