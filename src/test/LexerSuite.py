import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        testcase = '0asdasd'
        expect =  'asdasd,<EOF>'
        self.assertTrue(TestLexer.test(testcase, expect, 101))
