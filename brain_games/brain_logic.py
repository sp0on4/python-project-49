#!/usr/bin/env python3
import prompt


CYCLE_COUNT = 3


def engine(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.MANUAL)
    for i in range(CYCLE_COUNT):
        [question, true_answer] = game_module.brain_func()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
