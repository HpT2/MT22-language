import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        testcase =  """ "123 " """
        expect =  '343,<EOF>'
        print("123\r34")
        self.assertTrue(TestLexer.test(testcase, expect, 101))

        
