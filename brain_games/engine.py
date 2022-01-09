#!usr/bin/env python3
import prompt

from brain_games.cly import user_name

GAME_ROUNDS_COUNT = 3


def game_process(game: object) -> object:
    name = user_name()
    print(game.DESCRIPTION)
    for _ in range(GAME_SCORE):
        question, result = game.gen_question_and_result()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct')
        else:
            print('"{}" is wrong answer. Correct answer was "{}"'.format(answer, result))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
