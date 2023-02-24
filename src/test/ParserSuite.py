import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = 	"""a ="123";
        for (i[0] = 1 , i[0] < 2 , i[0] + -2){
        }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
