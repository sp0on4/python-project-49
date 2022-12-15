#!/usr/bin/env python3
from brain_games.brain_logic import game_logic
from brain_games.games.even import brain_func, MANUAL


def main():
    game_logic(brain_func, MANUAL)


if __name__ == '__main__':
    main()
