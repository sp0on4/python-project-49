#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint
import prompt


def main():
    name = welcome_user()  # приветствие и я так привязал переменную name
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        random_num = randint(1, 30)
        if random_num % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'
        print('Question:', random_num)
        answer = prompt.string('Your answe: ')
        if true_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
