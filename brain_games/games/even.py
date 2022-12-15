#!/usr/bin/env python3
from random import randint


MANUAL = 'Answer "yes" if the number is even, otherwise answer "no".'
START_VALUE = 1
FINISH_VALUE = 30


def brain_func():
    question = randint(START_VALUE, FINISH_VALUE)
    if question % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return (question, true_answer)
