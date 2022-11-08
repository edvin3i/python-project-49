#!/usr/bin/env python3

from random import randint
from math import gcd
from games.common_core import welcome_user
from games.common_core import game_cycle


def get_couple_nums():
    return f"{randint(0, 100)} {randint(0, 100)}"


def get_gcd(couple_nums):
    num1 = int(couple_nums.split()[0])
    num2 = int(couple_nums.split()[1])
    return str(gcd(num1, num2))


def start_gcd_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    questions = [get_couple_nums() for x in range(3)]
    right_answers = [get_gcd(couple) for couple in questions]
    game_cycle(name, questions, right_answers)
