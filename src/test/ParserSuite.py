import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              {
                  

            }"""
        expect = 'successful' 
        self.assertTrue(TestParser.test(input, expect, 207))
