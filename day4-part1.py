import re
from collections import Counter

__author__ = 'Richard Craggs'

def get_checksum(code):

    c = Counter(code)
    del c['-']

    letters_in_count_then_alpha_order = ""

    # loop over finding them in order of size
    for i in range(len(c), 0, -1):

        letters_of_this_length = []

        for letter, count in c.items():
            if count == i:
                letters_of_this_length.append(letter)

        letters_in_count_then_alpha_order += "".join(sorted(letters_of_this_length))

    return letters_in_count_then_alpha_order[0:5]


with open("./data/day4.txt") as f:
    content = f.readlines()

    sum_of_sectors = 0

    for line in content:
        m = re.search('(.*)-([0-9]+)\[([a-z]+)\]', line)

        if m.group(3) == get_checksum(m.group(1)):
            print("%s,%s" % (m.group(1), m.group(2)))
            sum_of_sectors += int(m.group(2))

    print(sum_of_sectors)