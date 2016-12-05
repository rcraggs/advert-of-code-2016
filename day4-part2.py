import re
from collections import Counter

__author__ = 'Richard Craggs'


def decrypt(letter, sector):

    if letter == '-':
        return ' '

    letter_pos = ord(letter) - 96
    letter_pos += sector
    letter_pos %= 26
    return_letter = chr(letter_pos + 96)
    return return_letter

with open("./data/day4-part2.txt") as f:
    content = f.readlines()

    sum_of_sectors = 0

    for line in content:
        code, sector = line.split(",")

        print("%s %s " % ("".join([decrypt(c, int(sector)) for c in code]), sector))