import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    """test ID"""
    def test1(self):
        testcase = " aBc a b2 _c1 _1 "
        expect = "aBc,a,b2,_c1,_1,<EOF>"
        self.assertTrue(TestLexer.test(testcase, expect, 101))

    """test INT_TYPE"""
    def test2(self):
        testcase = "1 123 98 01  123_45_6"
        expect = "1,123,98,0,1,123456,<EOF>"
        self.assertTrue(TestLexer.test(testcase, expect, 102))

    """test FLOAT_TYPE"""
    def test3(self):
        testcase = "1.E10 .e2 1.3 1_2.01 "
        expect = "1.E10,.e2,1.3,12.01,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,103))

    """test STRING_TYPE"""
    def test4(self):
        testcase = """ "abc123\\n" "AHS?_\\t321" "My id is 2012385" "\\\\ \\t \\f \\n \\r \\" \\'"  """
        expect = """abc123\\n,AHS?_\\t321,My id is 2012385,\\\\ \\t \\f \\n \\r \\" \\',<EOF>"""
        self.assertTrue(TestLexer.test(testcase,expect,104))

    """test COMMENT"""
    def test5(self):
        testcase = "//This is a 1 line comment"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,105))

    """test multiple lines comment """
    def test6(self):
        testcase = "/* This \n is \n a \n multiple \n line \n comment */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,106))

    """test seperators"""
    def test7(self):
        testcase = "(){}[].,;:="
        expect = "(,),{,},[,],.,,,;,:,=,<EOF>"    
        self.assertTrue(TestLexer.test(testcase,expect,107))

    """test operators"""
    def test8(self):
        testcase = "+ - * / % ! && || == != > >= < <="
        expect = "+,-,*,/,%,!,&&,||,==,!=,>,>=,<,<=,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,108))

    """test keywords"""
    def test9(self):
        testcase = """auto break boolean do else false 
                    float for function if integer return 
                    string true while void out continue of inherit array"""
        expect = "auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,109))

    """test ERROR_TOKEN"""
    def test10(self):
        testcase = "? abc"
        expect = "Error Token ?"
        self.assertTrue(TestLexer.test(testcase,expect,110))

    def test11(self):
        testcase = "123 @"
        expect = "123,Error Token @"
        self.assertTrue(TestLexer.test(testcase,expect,111))

    def test12(self):
        testcase = "./$*)("
        expect = ".,/,Error Token $"
        self.assertTrue(TestLexer.test(testcase,expect,112))

    def test13(self):
        testcase = "&&&"
        expect = "&&,Error Token &"
        self.assertTrue(TestLexer.test(testcase,expect,113))

    def test14(self):
        testcase = "^|"
        expect = "Error Token ^"
        self.assertTrue(TestLexer.test(testcase,expect,114))

    def test15(self):
        testcase = "|||||abc"
        expect = "||,||,Error Token |"
        self.assertTrue(TestLexer.test(testcase,expect,115))

    """test unclose string"""
    def test16(self):
        testcase = """ "abc123 """
        expect = "Unclosed String: abc123 "
        self.assertTrue(TestLexer.test(testcase,expect,116))      

    def test17(self):
        testcase = """ "\nabc123 """
        expect = "Unclosed String: "
        self.assertTrue(TestLexer.test(testcase,expect,117))

    def test18(self):
        testcase = """ "ab\ncd" """
        expect = "Unclosed String: ab"
        self.assertTrue(TestLexer.test(testcase,expect,118))

    def test19(self):
        testcase = """ "123\r321" """
        expect = "Unclosed String: 123"
        self.assertTrue(TestLexer.test(testcase,expect,119))

    def test20(self):
        testcase = """ "25/2\n\\v """
        expect = "Unclosed String: 25/2"
        self.assertTrue(TestLexer.test(testcase,expect,120))

    def test21(self):
        testcase = """ "tu\n\r\\v" """
        expect = "Unclosed String: tu"
        self.assertTrue(TestLexer.test(testcase,expect,121))

    def test22(self):
        testcase = """ "\\n\\t\\r\n\\f\\b" """
        expect = "Unclosed String: \\n\\t\\r"
        self.assertTrue(TestLexer.test(testcase,expect,122))

    def test23(self):
        testcase = """ "abcdef" \n \t "abc\t\tdef\n" """
        expect = "abcdef,Unclosed String: abc\t\tdef"
        self.assertTrue(TestLexer.test(testcase,expect,123))

    def test24(self):
        testcase = """ 123 "\rabc" 456 """
        expect = "123,Unclosed String: "
        self.assertTrue(TestLexer.test(testcase,expect,124))

    def test25(self):
        testcase = """ "\\t\nabc" """
        expect = "Unclosed String: \\t"
        self.assertTrue(TestLexer.test(testcase,expect,125))

    """test illegal escape"""
    def test26(self):
        testcase = """ "\\x" """
        expect = "Illegal Escape In String: \\x"
        self.assertTrue(TestLexer.test(testcase,expect,126))

    def test27(self):
        testcase = """ "\\c 123" """
        expect = "Illegal Escape In String: \\c"
        self.assertTrue(TestLexer.test(testcase,expect,127))

    def test28(self):
        testcase = """ "12\\c3" """
        expect = "Illegal Escape In String: 12\\c"
        self.assertTrue(TestLexer.test(testcase,expect,128))

    def test29(self):
        testcase = """ "abc\\n\\m\n123" """
        expect = "Illegal Escape In String: abc\\n\\m"
        self.assertTrue(TestLexer.test(testcase,expect,129))

    def test30(self):
        testcase = """ "\\m\nabc" """
        expect = "Illegal Escape In String: \\m"
        self.assertTrue(TestLexer.test(testcase,expect,130))

    def test31(self):
        testcase = """ "ab\\mc" """
        expect = "Illegal Escape In String: ab\\m"
        self.assertTrue(TestLexer.test(testcase,expect,131))

    def test32(self):
        testcase = """ "\\ " """
        expect = "Illegal Escape In String: \\ "
        self.assertTrue(TestLexer.test(testcase,expect,132))

    def test33(self):
        testcase = """ "\\w """
        expect = "Illegal Escape In String: \\w"
        self.assertTrue(TestLexer.test(testcase,expect,133))

    def test34(self):
        testcase = """ "ab\\ """
        expect = "Illegal Escape In String: ab\\ "
        self.assertTrue(TestLexer.test(testcase,expect,134))

    def test35(self):
        testcase = """ "a\\b\\t\\s\\n """
        expect = "Illegal Escape In String: a\\b\\t\\s"
        self.assertTrue(TestLexer.test(testcase,expect,135))

    """random test"""
    def test36(self):
        testcase = """ a1 "123" print """
        expect = "a1,123,print,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,136))
    
    def test37(self):
        testcase = """ if (a>1) do a + 2 """
        expect = "if,(,a,>,1,),do,a,+,2,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,137))

    def test38(self):
        testcase = """ for _j_ and " or """
        expect = "for,_j_,and,Unclosed String:  or "
        self.assertTrue(TestLexer.test(testcase,expect,138))

    def test39(self):
        testcase = """ a = a + b[2] """
        expect = "a,=,a,+,b,[,2,],<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,139))

    def test40(self):
        testcase = "a:integer = 10;"
        expect = "a,:,integer,=,10,;,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,140))

    def test41(self):
        testcase = """ "a" + 1. """
        expect = "a,+,1.,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,141))

    def test42(self):
        testcase = """do {x % 0_7_9}"""
        expect = "do,{,x,%,0,_7_9,},<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,142))

    def test43(self):
        testcase = """ <EOF> """
        expect = "<,EOF,>,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,143))

    def test44(self):
        testcase = """ \n\\t """
        expect = "Error Token \\"
        self.assertTrue(TestLexer.test(testcase,expect,144))

    def test45(self):
        testcase = """ fact: function float () """
        expect = "fact,:,function,float,(,),<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,145))

    def test46(self):
        testcase = """ a\t "" """
        expect = "a,,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,146))

    def test47(self):
        testcase = """ "20"::"12 HCM,city"""
        expect = "20,::,Unclosed String: 12 HCM,city"
        self.assertTrue(TestLexer.test(testcase,expect,147))

    def test48(self):
        testcase = """ 1_e10 """
        expect = "1,_e10,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,148))

    def test49(self):
        testcase = """ 123_abc.de-10 """
        expect = "123,_abc,.,de,-,10,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,149))

    def test50(self):
        testcase = """ .E.E-30 """
        expect = ".,E,.E-30,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,150))

    def test51(self):
        testcase = 	"1_234.E "
        expect = "1234.,E,<EOF>"
        self.assertTrue(TestLexer.test(testcase, expect, 151))

    def test52(self):
        testcase = "098_a"
        expect = "0,98,_a,<EOF>"
        self.assertTrue(TestLexer.test(testcase, expect, 152))

    def test53(self):
        testcase = "1_"
        expect = "1,_,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,153))

    def test54(self):
        testcase = """ stri_"123\\t"||' """
        expect = "stri_,123\\t,||,Error Token '"
        self.assertTrue(TestLexer.test(testcase,expect,154))

    def test55(self):
        testcase = "//abc\n ___"
        expect = "___,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,155))

    def test56(self):
        testcase = "/*%^%?() hhjdsf//><sa*/ \n int i = 10"
        expect = "int,i,=,10,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,156))

    def test57(self):
        testcase = "7E9*0e.2"
        expect = "7E9,*,0,e,.,2,<EOF>"    
        self.assertTrue(TestLexer.test(testcase,expect,157))

    def test58(self):
        testcase = ""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,158))

    def test59(self):
        testcase = "print(x)"
        expect = "print,(,x,),<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,159))

    def test60(self):
        testcase = """ Python is fun"?" """
        expect = "Python,is,fun,?,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,160))

    def test61(self):
        testcase = "if this: \\t, then That_"
        expect = "if,this,:,Error Token \\"
        self.assertTrue(TestLexer.test(testcase,expect,161))

    def test62(self):
        testcase = """ "This cost" _9 "$"  """
        expect = "This cost,_9,$,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,162))

    def test63(self):
        testcase = "do{a+b}\"@#$ "
        expect = "do,{,a,+,b,},Unclosed String: @#$ "
        self.assertTrue(TestLexer.test(testcase,expect,163))

    def test64(self):
        testcase = "\t\r\n "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,164))

    def test65(self):
        testcase = "true||false_1e10"
        expect = "true,||,false_1e10,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,165))

    def test66(self):
        testcase = """ 123_.e-9 """
        expect = "123,_,.e-9,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,166))      

    def test67(self):
        testcase = """ 123-.e_-9 """
        expect = "123,-,.,e_,-,9,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,167))

    def test68(self):
        testcase = """ "Love_u3k" """
        expect = "Love_u3k,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,168))

    def test69(self):
        testcase = """ /*/*/* abc */"""
        expect = "*,abc,*,/,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,169))

    def test70(self):
        testcase = """ a=c\d """
        expect = "a,=,c,Error Token \\"
        self.assertTrue(TestLexer.test(testcase,expect,170))

    def test71(self):
        testcase = """ I'm a handsome boy"""
        expect = "I,Error Token '"
        self.assertTrue(TestLexer.test(testcase,expect,171))

    def test72(self):
        testcase = "dlrow eht fo dne llit u e^ol"
        expect = "dlrow,eht,fo,dne,llit,u,e,Error Token ^"
        self.assertTrue(TestLexer.test(testcase,expect,172))

    def test73(self):
        testcase = "for(int i = 1;i<2;i++)"
        expect = "for,(,int,i,=,1,;,i,<,2,;,i,+,+,),<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,173))

    def test74(self):
        testcase = """ \r hhaha_1_.98e1 """
        expect = "hhaha_1_,.98e1,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,174))

    def test75(self):
        testcase = """ 9_8_7_6_5_____4 """
        expect = "98765,_____4,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,175))

    def test76(self):
        testcase = """ " """
        expect = "Unclosed String:  "
        self.assertTrue(TestLexer.test(testcase,expect,176))

    def test77(self):
        testcase = """ Uoc 01_0 diem PPL """
        expect = "Uoc,0,10,diem,PPL,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,177))

    def test78(self):
        testcase = """ while(false){} """
        expect = "while,(,false,),{,},<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,178))

    def test79(self):
        testcase = """ main:function void(){} """
        expect = "main,:,function,void,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,179))

    def test80(self):
        testcase = """ a[0]= "123" """
        expect = "a,[,0,],=,123,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,180))

    def test81(self):
        testcase = """ "\\t\\r\\n\\f\\b\\'\\"\\\\" """
        expect = """\\t\\r\\n\\f\\b\\'\\"\\\\,<EOF>"""
        self.assertTrue(TestLexer.test(testcase,expect,181))

    def test82(self):
        testcase = """ //Acomment "//g" """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,182))

    def test83(self):
        testcase = """ "luv u" <3 """
        expect = "luv u,<,3,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,183))

    def test84(self):
        testcase = """ a\nb\nc\n""\r  """
        expect = "a,b,c,,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,184))

    def test85(self):
        testcase = """ "a""b""c""d"  """
        expect = "a,b,c,d,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,185))

    def test86(self):
        testcase = """ " "" " " "" " """
        expect = " , , , ,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,186))
    
    def test87(self):
        testcase = """  "" "" "" "" """
        expect = ",,,,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,187))

    def test88(self):
        testcase = """ _1_E-8.Ea_1 """
        expect = "_1_E,-,8.,Ea_1,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,188))

    def test89(self):
        testcase = """ char* a """
        expect = "char,*,a,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,189))

    def test90(self):
        testcase = """::a:"\\g" """
        expect = "::,a,:,Illegal Escape In String: \\g"
        self.assertTrue(TestLexer.test(testcase,expect,190))

    def test91(self):
        testcase = """ _1 + 1e + 1. """
        expect = "_1,+,1,e,+,1.,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,191))

    def test92(self):
        testcase = """ 9%2 == !(true) """
        expect = "9,%,2,==,!,(,true,),<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,192))

    def test93(self):
        testcase = """ "{}\\" """
        expect = """Unclosed String: {}\\" """
        self.assertTrue(TestLexer.test(testcase,expect,193))

    def test94(self):
        testcase = """ "8_8" 8_8 """
        expect = "8_8,88,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,194))

    def test95(self):
        testcase = """ ;;;,o """
        expect = ";,;,;,,,o,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,195))

    def test96(self):
        testcase = """return n*n """
        expect = "return,n,*,n,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,196))

    def test97(self):
        testcase = """ HCMC_HCMUT """
        expect = "HCMC_HCMUT,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,197))

    def test98(self):
        testcase = """ 9999_()e10 """
        expect = "9999,_,(,),e10,<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,198))

    def test99(self):
        testcase = """ m.%!~&| """
        expect = "m,.,%,!,Error Token ~"
        self.assertTrue(TestLexer.test(testcase,expect,199))

    def test100(self):
        testcase = """ ' """
        expect = "Error Token '"
        self.assertTrue(TestLexer.test(testcase,expect,200))