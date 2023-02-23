import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = 	""" fact: function array [2] of integer (n: array [-1,2,3,4,5] of integer) {
            if (n == 0) { {a= a[2+3,b[2]];}
            }
            else return n * fact(n - 1);
            a,b: integer = {1,2},2 ;
        } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
