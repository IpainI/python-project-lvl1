import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_result():

    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    result = str(math.gcd(number1, number2))
    expression = '{} {} '.format(number1, number2)
    return expression, result
