#!/usr/bin/env python3

from brain_games.games import prime
from brain_games.engine import game_process


def main() -> object:
    game_process(prime)


if __name__ == '__main__':
    main()
