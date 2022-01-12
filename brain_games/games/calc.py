import random

DESCRIPTION = 'What is the result of the expression?'
ALLOWED_OPERATIONS = ['+', '-', '*']


def get_question_and_result():

    operation = random.choice(ALLOWED_OPERATIONS)
    number1 = random.randint(1, 40)
    number2 = random.randint(1, 40)
    if operation == '+':
        result = str(number1 + number2)
    elif operation == '-':
        result = str(number1 - number2)
    elif operation == '*':
        result = str(number1 * number2)
    expression = 'Question: {} {} {}'.format(number1, operation, number2)
    return expression, result
