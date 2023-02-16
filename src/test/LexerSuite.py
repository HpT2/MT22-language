import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        testcase = '7'
        expect =  '7,<EOF>'
        self.assertTrue(TestLexer.test(testcase, expect, 101))
