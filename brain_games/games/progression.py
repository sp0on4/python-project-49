#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint
import prompt

name = welcome_user()


def progression_func():
    print('What number is missing in the progression?')

    for _ in range(3):
        start = randint(1, 5)
        stop = randint(25, 30)
        step = randint(3, 4)
        result = []
        for num in range(start, stop, step):
            result.append(num)
        index = randint(0, len(result)-1)
        true_answer = str(result[index])
        result[index] = '..'
        print('Question:', " ".join(map(str, result)))
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
