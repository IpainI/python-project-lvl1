#!/usr/bin/env python3

from brain_games.games import calc
from brain_games.engine import start_game_process


def main():
    print('Welcome to the Brain Games!')
    start_game_process(calc)


if __name__ == '__main__':
    main()
