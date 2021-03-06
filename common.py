# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):
    lowerletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spec = ['<', '>', '#', '&', '@', '{', '}', ',', '"', "'", '?',
            '.', ':', '-', '_', '+', '!', '%', '/', '=', '(', ')', '|']

    generated = ""
    while generated == "":

        generated += random.choice(lowerletters)
        generated += random.choice(upperletters)
        generated += random.choice(numbers)
        generated += random.choice(numbers)
        generated += random.choice(upperletters)
        generated += random.choice(lowerletters)
        generated += random.choice(spec)
        generated += random.choice(spec)
        for line in table:
            if generated == line[0]:
                generated = ""

    return generated
