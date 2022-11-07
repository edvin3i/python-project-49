#!/usr/bin/env python3

import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def is_even(num):
    if num % 2:
        return 'no'
    return 'yes'


def ask_question(num):
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    return answer


def start_game():
    name = welcome_user()
    try_num = 1

    while try_num <= 3:
        num = randint(1, 100)
        user_answer = ask_question(num).lower()
        right_answer = is_even(num)
        if right_answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{right_answer}'.")
            print("Let's try again, {name}!")
            return
        try_num += 1
    print(f'Congratulations, {name}!')


def main():
    print("Welcome to the Brain Games!")
    start_game()


if __name__ == '__main__':
    main()
