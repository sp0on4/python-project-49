#!/usr/bin/env python3
from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_VALUE = 2
FINISH_VALUE = 20


def brain_func():
    question = randint(START_VALUE, FINISH_VALUE)
    true_answer = 'yes'
    if is_prime(question):
        true_answer = 'no'
        return question, true_answer
    return question, true_answer


def is_prime(number):
    for del_num in range(2, number // 2 + 1):
        if number % del_num == 0:
            return del_num
