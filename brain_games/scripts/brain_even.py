#!/usr/bin/env python3
from brain_games.brain_logic import generate_a_game
from brain_games.games import even


def main():
    generate_a_game(even)


if __name__ == '__main__':
    main()
