import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        testcase = """ "\\ " """
        expect =  '1.E12,<EOF>'
        print(testcase)
        self.assertTrue(TestLexer.test(testcase, expect, 101))

        
