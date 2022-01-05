#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games.engine import game_process


def main() -> object:
    print('Welcome to the Brain Games!')
    game_process(gcd)


if __name__ == '__main__':
    main()
