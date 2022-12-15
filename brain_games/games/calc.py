#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint
import prompt

name = welcome_user()


def calc_func():
    print('What is the result of the expression?')

    for _ in range(3):
        num1 = randint(1, 15)
        num2 = randint(1, 15)
        lst = ['+', '-', '*']
        index = randint(0, len(lst) - 1)
        if index == 0:
            print('Question:', num1, lst[index], num2)
            answer = prompt.string('Your answer: ')
            true_answer = str(num1 + num2)
        if index == 1:
            print('Question:', num1, lst[index], num2)
            answer = prompt.string('Your answer: ')
            true_answer = str(num1 - num2)
        if index == 2:
            print('Question:', num1, lst[index], num2)
            answer = prompt.string('Your answer: ')
            true_answer = str(num1 * num2)
        if true_answer == answer:
            print('Correct!')
        else:
            game_end(answer, true_answer, name)
            return
    print(f'Congratulations, {name}!')


def game_end(answer, true_answer, name):
    print(f"'{answer}' is wrong answer ;(. "
          f"Correct answer was '{true_answer}'.")
    print(f"Let's try again, {name}!")
