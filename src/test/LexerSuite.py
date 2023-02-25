import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        testcase = """ "if ( i == 1 ) \nreturn 2 ;" """
        expect =  'if,(,i,==,1,),return,2,;,<EOF>'
        print(testcase)
        self.assertTrue(TestLexer.test(testcase, expect, 101))

        
