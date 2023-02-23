import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        testcase = """ {return "123";
                       a=123;}
                        return "12"; """
        expect =  '\\\',<EOF>'
        print(testcase)
        self.assertTrue(TestLexer.test(testcase, expect, 101))

        
