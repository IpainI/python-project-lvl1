import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):

    count = 0

    for i in range(1, number // 2 + 1):
        if number % i == 0:
            count += 1
            if count > 2 or number == 1:
                return 'no'
    return 'yes'


def gen_question_and_result():

    number = random.randint(1, 50)
    result = is_prime(number)
    expression = 'Question: {}'.format(number)
    return expression, result
