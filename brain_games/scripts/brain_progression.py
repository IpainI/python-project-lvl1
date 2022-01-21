#!/usr/bin/env python3

from brain_games.games import progression
from brain_games.engine import start_game_process


def main():
    print('Welcome to the Brain Games!')
    start_game_process(progression)


if __name__ == '__main__':
    main()
