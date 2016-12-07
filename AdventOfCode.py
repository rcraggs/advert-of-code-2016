import hashlib
from collections import Counter
import re

__author__ = 'Richard Craggs'


class AdventOfCode:

    current_index = 0

    # --- Day 5

    def find_next_hash(self, door_id):

        m = hashlib.md5((door_id + str(self.current_index)).encode())

        while m.hexdigest()[0:5] != "00000":

            m = hashlib.md5((door_id + str(self.current_index)).encode())
            self.current_index += 1

        return m.hexdigest()

    def get_next_digit(self, door_id):
        return self.find_next_hash(door_id)[5]

    def get_password(self, door_id, length):

        self.current_index = 0
        password = ""

        for i in range(1, length+1):
            password += self.get_next_digit(door_id)

        return password

    def get_password_2(self, door_id, length):

        self.current_index = 0
        password = {}

        while len(password) <= 7:

            next_hash = self.find_next_hash(door_id)

            position = next_hash[5]
            digit = next_hash[6]

            if int(position, 16) < length and position not in password.keys():
                password[position] = digit
                print(password)
            else:
                print("rejecting " + digit + " for position " + position)

        password_text = ""
        for k in sorted(password):
            password_text += password[k]

        print(password)
        return password_text

    # --- Day 6

    def day_6_aux(self, message, position_in_counter):
        word_length = len(message[0])
        num_rows = len(message)
        word = ""
        for i in range(0, word_length - 1):
            c = Counter([line[i] for line in message])
            word += c.most_common(num_rows)[position_in_counter][0]
        return word

    def get_day_6_word(self, message):
        return self.day_6_aux(message, 0)


    def get_day_6_part_2_word(self, message):
        return self.day_6_aux(message, -1)

    def is_ip_abba(self, addr):

        addr = addr.rstrip()

        # if the IP contains abba in brackets then it's not
        match = re.search(r'\[[^\]]*(\w)(\w)(?!\1)(\2)(\1)[^\]]*\]', addr)
        if match:
            # print("NOINBR} " + addr + " : " + match.group(0))
            return False

        pattern = re.compile(r'(\w)(\w)(?!\1)\2\1')
        match = pattern.search(addr)

        # if match:
        #     # print("YESABBA} " + addr + " : " + match.group(0))
        # else:
        #     # print("NOWT} " + addr )

        return bool(match)

