import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """fact: function integer (){
              if(true) return;
              a = {1,2,3};
        }"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 207))
