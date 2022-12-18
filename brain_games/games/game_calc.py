from random import randint, choice
import operator


MSG_RULES = 'What is the result of the expression?'
OPERATIONS = (
    ("+", operator.add),
    ("-", operator.sub),
    ("*", operator.mul),
)


def get_expression() -> tuple:
    """Returns random expression for two numbers and random action(+, -, *)."""
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operation_sym, operation_fn = choice(OPERATIONS)
    question = f"{num1} {operation_sym} {num2}"
    right_answer = operation_fn(num1, num2)
    return question, right_answer


def get_quiz() -> tuple:
    return get_expression()
