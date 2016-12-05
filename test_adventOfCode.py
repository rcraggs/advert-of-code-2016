from unittest import TestCase
from AdventOfCode import AdventOfCode

__author__ = 'Richard Craggs'


class TestAdventOfCode(TestCase):
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
