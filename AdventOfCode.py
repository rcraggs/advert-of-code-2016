import hashlib
from collections import Counter
import re
import numpy as np

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
            return False

        pattern = re.compile(r'(\w)(\w)(?!\1)\2\1')
        match = pattern.search(addr)

        return bool(match)

    def is_ip_aba(self, addr):

        addr = addr.rstrip()

        hyper_a = re.sub('\[[^\]]+\]', "", addr) # without the bracket bits
        sub_a = "".join(re.findall("\[[^\]]+]", addr)) # just the bracket bits

        print("hyper " + hyper_a)
        print("sub " + sub_a)

        # get a list of the abas in the hyper_as, then switch them
        abas = [x[0] for x in re.findall("((\w)\w\\2)", hyper_a)]

        print("abas %s" % abas)

        babs = [list(o)[1]+list(o)[0]+list(o)[1] for o in abas]

        print("babs %s" % babs)

        if any(x in sub_a for x in babs):
            return True
        else:
            return False


    screen = None

    def process_screen_instructions(self, instructions, columns, rows):


        rect_instr = re.compile(r'^rect\s([0-9]+)x([0-9]+)$')
        move_instr = re.compile(r'rotate (row|column) (x|y)=([0-9]+) by ([0-9]+)')

        # initialise the screen to the correct size
        self.screen = np.zeros((rows, columns))

        # Process the instructions
        for instruction in instructions:

            match = rect_instr.match(instruction)

            if match:
                rect_cols = int(match.group(1))
                rect_rows = int(match.group(2))
                ones = np.ones((rect_rows, rect_cols))
                self.screen[:ones.shape[0], :ones.shape[1]] = ones

                print("rect %s, %s" % (rect_cols, rect_rows))
            else:
                match = move_instr.match(instruction)

                if match.group(1) == 'row':
                    shift = int(match.group(4))
                    row = int(match.group(3))
                    row_data = self.screen[row]
                    row_data = np.concatenate((row_data[shift*-1:],row_data[:shift*-1]),0)
                    self.screen[row] = row_data

                else:
                    column = int(match.group(3))
                    shift = int(match.group(4))
                    print("col %s -> %s" % (column, shift))
                    col = self.screen[:, column:column+1]

                    q_top = col[:-1*shift]
                    q_bot = col[-1*shift:]

                    new_q = np.concatenate((q_bot, q_top),0)
                    self.screen[:, column:column+1] = new_q

                print(self.screen)
                np.savetxt("foo.csv", self.screen, delimiter=",", format='%10f')

    def get_lit_pixels(self):
        return np.count_nonzero(self.screen)



    def get_decompressed_length(self, message):

        decompressed_length = 0

        splitter = re.compile("^([^\(]*)\((\d+)x(\d+)\)(.*)")
        match = splitter.match(message)

        while match:

            # print("remaining string " + match.group(4))

            # Add everything up to the next marker to the length
            decompressed_length += len(match.group(1))

            num_chars_to_repeat = int(match.group(2))
            repetitions = int(match.group(3))

            # remove the characters that we're going to repeat
            message = match.group(4)[num_chars_to_repeat:]

            # add how many characters would result from repeating them
            decompressed_length += num_chars_to_repeat * repetitions

            # Split again
            match = splitter.match(message)

        # Add the rest of the message to the length
        decompressed_length += len(message)

        return decompressed_length

    def get_decompressed_length_2(self, message):

        decompressed_length = 0

        splitter = re.compile("^([^\(]*)\((\d+)x(\d+)\)(.*)")
        match = splitter.match(message)

        while match:

            # print("remaining string " + match.group(4))

            # Add everything up to the next marker to the length
            decompressed_length += len(match.group(1))

            num_chars_to_repeat = int(match.group(2))
            repetitions = int(match.group(3))

            new_repeated_bit = match.group(4)[:num_chars_to_repeat]
            tail_of_the_message = match.group(4)[num_chars_to_repeat:]

            # remove the characters that we're going to repeat
            message = str((new_repeated_bit * repetitions) + tail_of_the_message)

            # add how many characters would result from repeating them
            # decompressed_length += num_chars_to_repeat * repetitions

            # Split again
            match = splitter.match(message)

            if decompressed_length % 1000 == 0:
                print("current so far " + str(decompressed_length))
                print("remaining message length %s " % len(message))

        # Add the rest of the message to the length
        decompressed_length += len(message)

        return decompressed_length