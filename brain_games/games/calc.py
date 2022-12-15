#!/usr/bin/env python3
from random import randint


MANUAL = 'What is the result of the expression?'
START_VALUE1 = 1
FINISH_VALUE1 = 15
START_VALUE2 = 1
FINISH_VALUE2 = 15
LIST_OPERATIONS = ['+', '-', '*']


def brain_func():
    num1 = randint(START_VALUE1, FINISH_VALUE1)
    num2 = randint(START_VALUE2, FINISH_VALUE2)
    index = randint(0, len(LIST_OPERATIONS) - 1)
    question = f'{num1} {LIST_OPERATIONS[index]} {num2}'
    if index == 0:
        true_answer = str(num1 + num2)
    if index == 1:
        true_answer = str(num1 - num2)
    if index == 2:
        true_answer = str(num1 * num2)
    return question, true_answer
