import random

DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def gen_question_and_result():

    number = random.randint(1, 100)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    expression = 'Question: {}'.format(number)
    return expression, result
