import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = 	"""x: integer = 65;
        fact: function integer (n: integer) {
            a = "\\n as" ;
            foo(2 + x, 4.0 / y);
            a= a-1;
            goo();
            a = a[b[1,2],2,c[5,0]] ;
            x: integer = 1;
            if (n == 0) {return 1;return 2;}
            else return n * fact(n - 1);
            while(b){}
            do{
                writeLn(i);
                a = 2;
                continue;
                for ( i = 1 , i < 10 , i + 1){
                    while(true){return 2;}
                }
            }while(true);
            return 2;
            {
                print(123);
                a : integer = 1;
            }
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
