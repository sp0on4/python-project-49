#!/usr/bin/env python3
from random import randint
import math


MANUAL = 'Find the greatest common divisor of given numbers.'
START_VALUE1 = 1
FINISH_VALUE1 = 15
START_VALUE2 = 1
FINISH_VALUE2 = 15


def brain_func():
    num1 = randint(START_VALUE1, FINISH_VALUE1)
    num2 = randint(START_VALUE2, FINISH_VALUE2)
    question = f'{num1} {num2}'
    true_answer = str(math.gcd(num1, num2))
    return question, true_answer
