import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = 	"""x: integer = 65;
        fact: function integer (n: integer) {
            a = a + 2;
            x: integer = 65;
            if (n == 0) return 1;
            else return n * fact(n - 1);
            for_stmt 
            while_stmt
            return 2;
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
