import random

DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = ['+', '-', '*']


def gen_question_and_result():

    operation = random.choice(OPERATIONS)
    if operation == '+':
        number1 = random.randint(1, 40)
        number2 = random.randint(1, 40)
        result = str(number1 + number2)
    elif operation == '-':
        number1 = random.randint(1, 40)
        number2 = random.randint(1, 40)
        result = str(number1 - number2)
    elif operation == '*':
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 20)
        result = str(number1 * number2)
    expression = 'Question: {} {} {}'.format(number1, operation, number2)
    return expression, result
