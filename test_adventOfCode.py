from unittest import TestCase
from AdventOfCode import AdventOfCode

__author__ = 'Richard Craggs'


class TestAdventOfCode(TestCase):

    a = None

    def setUp(self):
        self.a = AdventOfCode()

    def test_getNextDigit(self):
        a = AdventOfCode()
        self.assertEqual(a.get_next_digit("abc"), "1")
        self.assertEqual(a.get_next_digit("abc"), "8")

    def test_getPassword(self):
        a = AdventOfCode()
        self.assertEqual(a.get_password("abc", 8), "18f47a30")

    def test_get_result(self):
        a = AdventOfCode()
        print(a.get_password("ojvtpuvg", 8))
        self.assertEqual(1, 1)

    def test_get_password_2(self):
        a = AdventOfCode()
        self.assertEqual(a.get_password_2("abc", 8), "05ace8e3")

    def test_get_result_2(self):
        a = AdventOfCode()
        print(a.get_password_2("ojvtpuvg", 8))
        self.assertEqual(1, 1)

    def test_get_day_6_test_word(self):

        f = open("./data/day6-test.txt")
        message = f.readlines()

        self.assertEqual(self.a.get_day_6_word(message), "easter")


    def test_get_day_6_word(self):

        f = open("./data/day6.txt")
        message = f.readlines()
        print(self.a.get_day_6_word(message))
        self.assertEqual("easter", "easter")


    def test_get_day_6_part_2_test_word(self):

        f = open("./data/day6-test.txt")
        message = f.readlines()

        self.assertEqual(self.a.get_day_6_part_2_word(message), "advent")


    def test_get_day_6_part_2_word(self):

        f = open("./data/day6.txt")
        message = f.readlines()
        print(self.a.get_day_6_part_2_word(message))
        self.assertEqual("easter", "easter")


    def test_day_7_part_1(self):

        self.assertEquals(self.a.is_ip_abba(r"abba[mnop]qrst"), True)
        self.assertEquals(self.a.is_ip_abba(r"ioxxoj[asdfgh]zxcvbn"), True)
        self.assertEquals(self.a.is_ip_abba(r"abcd[bddb]xyyx"), False)
        self.assertEquals(self.a.is_ip_abba(r"aaaa[qwer]tyui"), False)

    def test_day_7_part_2(self):

        self.assertEquals(self.a.is_ip_aba(r"aba[bab]xyz"), True)
        self.assertEquals(self.a.is_ip_aba(r"xyx[xyx]xyx"), False)
        self.assertEquals(self.a.is_ip_aba(r"aaa[kek]eke"), True)
        self.assertEquals(self.a.is_ip_aba(r"zazbz[bzb]cdb"), True)

    def test_day_7_2_inside(self):
        self.assertEquals(self.a.is_ip_aba(r"oktlpryceitvhqqjqxq[ufupbpapoxovifhqp]xgrwutvfooowfaxs[yxoxzdoqyhxsiwcxrgm]swmalhlzrknfxgnamr"), False)


    def test_run_day_7_part_1(self):

        f = open("./data/day7.txt")
        ips = f.readlines()
        print(sum(self.a.is_ip_aba(ip) for ip in ips))


    def test_8_1(self):

        instructions = ("rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1")

        self.a.process_screen_instructions(instructions, 7, 3)
        self.assertEqual(self.a.get_lit_pixels(), 6)

    def test_run_8_1(self):

        f = open("./data/day8.txt")
        instructions = f.readlines()
        self.a.process_screen_instructions(instructions, 50, 6)
        print(self.a.get_lit_pixels())

