#!/usr/bin/env python3
from random import randint


MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_VALUE = 2
FINISH_VALUE = 20


def brain_func():
    question = randint(START_VALUE, FINISH_VALUE)
    true_answer = 'yes'
    for del_num in range(2, question // 2 + 1):
        if question % del_num == 0:
            true_answer = 'no'
    return question, true_answer
