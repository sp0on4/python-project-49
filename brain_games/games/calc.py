#!/usr/bin/env python3
from random import randint, choice


RULES = 'What is the result of the expression?'
START_VALUE1 = 1
FINISH_VALUE1 = 15
START_VALUE2 = 1
FINISH_VALUE2 = 15
LIST_OPERATIONS = ['+', '-', '*']


def brain_func():
    num1 = randint(START_VALUE1, FINISH_VALUE1)
    num2 = randint(START_VALUE2, FINISH_VALUE2)
    operation = get_operation()
    question = f'{num1} {operation} {num2}'
    true_answer = get_true_answer(operation, num1, num2)
    return question, true_answer


def get_operation():
    return choice(LIST_OPERATIONS)


def get_true_answer(operation, num1, num2):
    if operation == '+':
        true_answer = str(num1 + num2)
        return true_answer
    if operation == '-':
        true_answer = str(num1 - num2)
        return true_answer
    if operation == '*':
        true_answer = str(num1 * num2)
        return true_answer
