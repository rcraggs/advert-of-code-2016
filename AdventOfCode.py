import hashlib

__author__ = 'Richard Craggs'

class AdventOfCode:

    current_index = 0

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
