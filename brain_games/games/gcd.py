import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_result():

    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = str(math.gcd(number1, number2))
    expression = 'Question: {} {} '.format(number1, number2)
    return expression, result
