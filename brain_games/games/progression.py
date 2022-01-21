import random

DESCRIPTION = 'What number is missing in the progression?'


def get_progression():
    length = random.randint(5, 15)
    step = random.randint(1, 10)
    first = random.randint(1, 15)
    progression = [first + step * i for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    result = ".."
    progression[hidden_index], result = result, progression[hidden_index]
    return ' '.join(map(str, progression)), str(result)


def get_question_and_result():
    progression, result = get_progression()
    expression = '{}'.format(progression)
    return expression, result
