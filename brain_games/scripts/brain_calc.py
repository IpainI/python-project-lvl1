#!/usr/bin/env python3

from brain_games.games import calc
from brain_games.engine import game_process


def main() -> object:
    print('Welcome to the Brain Games!')
    game_process(calc)


if __name__ == '__main__':
    main()
