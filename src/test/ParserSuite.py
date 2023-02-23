import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = 	"""{
            r,s: integer;
            r = 2.0;
            a,b : array [5] of integer = {1,2,3},{3};
            s = r * r * myPI;
            a[0] = s;
        } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
