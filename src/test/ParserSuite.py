import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = 	"""
          fact: function integer (){
              do {x =2 ;}
              while(b[3-2 + -(1234-2)]);
              a = 1.0e10;
              a[foo(2)]=1;
              a: integer;
          }

         """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
