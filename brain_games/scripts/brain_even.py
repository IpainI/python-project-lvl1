#!/usr/bin/env python3

from brain_games.games import even
from brain_games.engine import game_process


def main():
    print('Welcome to the Brain Games!')
    game_process(even)


if __name__ == '__main__':
    main()
