#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint
import prompt

name = welcome_user()


def prime_func():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):
        num = randint(2, 20)
        true_answer = 'yes'
        for del_num in range(2, num//2+1):
            if num % del_num == 0:
                true_answer = 'no'
        print('Question:', num)
        answer = prompt.string('Your answer: ')
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
