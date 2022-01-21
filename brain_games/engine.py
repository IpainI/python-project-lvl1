#!usr/bin/env python3
import prompt

from brain_games.cli import ask_user_name

GAME_ROUNDS_COUNT = 3


def game_process(game):
    name = ask_user_name()
    print(game.DESCRIPTION)
    for _ in range(GAME_ROUNDS_COUNT):
        question, result = game.get_question_and_result()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct')
        else:
            print('"{}" is wrong answer. Correct answer was "{}".'.format(answer, result))
            print("Let's try again, {}!".format(name))
            return
    print('Congratulations, {}!'.format(name))
