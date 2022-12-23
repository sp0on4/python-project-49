#!/usr/bin/env python3
from random import randint


RULES = 'What number is missing in the progression?'
START_VALUE1 = 1
FINISH_VALUE1 = 5
START_VALUE2 = 25
FINISH_VALUE2 = 30
START_VALUE3 = 3
FINISH_VALUE3 = 4


def brain_func():
    start = randint(START_VALUE1, FINISH_VALUE1)
    stop = randint(START_VALUE2, FINISH_VALUE2)
    step = randint(START_VALUE3, FINISH_VALUE3)
    list_progression = get_progression(start, stop, step)
    true_answer, question = get_question(list_progression)
    return question, true_answer


def get_progression(start, stop, step):
    result = []
    for num in range(start, stop, step):
        result.append(num)
    return result


def get_question(result):
    index = randint(0, len(result) - 1)
    true_answer = str(result[index])
    result[index] = '..'
    question = " ".join(map(str, result))
    return true_answer, question
