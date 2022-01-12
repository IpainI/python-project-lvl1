import random

DESCRIPTION = 'What number is missing in the progression?'


def get_progression():
    length = random.randint(5, 15)
    step = random.randint(1, 10)
    first = random.randint(1, 15)
    progression = [first + step * i for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    hidden_item = ".."
    progression[hidden_index], hidden_item = hidden_item, progression[hidden_index]
    return progression, str(hidden_item)


def get_question_and_result():
    progression, result = get_progression()
    expression = 'Question: {} '.format(progression)
    return expression, result
