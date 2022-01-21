import random

DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def get_question_and_result():

    number = random.randint(1, 100)
    result = ['yes' if number % 2 == 0 else 'no']
    expression = '{}'.format(number)
    return expression, *result
