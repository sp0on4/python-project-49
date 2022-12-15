#!/usr/bin/env python3
import prompt


CYCLE_COUNT = 3


def game_logic(brain_func, MANUAL):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(MANUAL)
    for i in range(CYCLE_COUNT):
        [question, true_answer] = brain_func()
        print('Question:', question)
        answer = ''
        print('Your answer: ', end='')
        answer = input()
        if answer == str(true_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{true_answer}'.")
            print("Let's try again, {}!".format(name))
            return
    print('Congratulations, {}!'.format(name))
