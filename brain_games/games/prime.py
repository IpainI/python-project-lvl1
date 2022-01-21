import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_result():
    number = random.randint(1, 50)
    result = 'yes' if is_prime(number) else 'no'
    expression = '{}'.format(number)
    return expression, result
