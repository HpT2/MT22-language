import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = 	"""
          for(i=1,true,i+2){
            continue;
          }
          a["a"] = 2;

         """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
