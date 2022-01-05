import random

DESCRIPTION = 'What number is missing in the progression?'


def gen_progression(leght):

    progression = []
    step = random.randint(1, 5)
    first = random.randint(1, 15)
    for i in range(leght):
        progression.append(first + step * i)
    hide = random.randint(1, leght)
    key = ".."
    progression[hide], key = key, progression[hide]
    return progression, str(key)


def gen_question_and_result():

    leght = random.randint(5, 10)
    progression, result = gen_progression(leght)
    expression = 'Question: {} '.format(*progression)
    return expression, result
