import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        testcase = """ 1_2E10 """
        expect =  '<EOF>'
        print(testcase)
        self.assertTrue(TestLexer.test(testcase, expect, 101))

        
