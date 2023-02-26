import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    
    def test1(self):
        """test variable declaration"""
        input = """ a,b,c : string; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    def test2(self):
        input = """ a,b,c : string = "a","b","c"; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test3(self):
        input = """a,b,c : string = "a","b","c","d"; """
        expect = "Error on line 1 col 28: ,"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test4(self):
        input = """ a,b,c,d : string = 1,2,3; """
        expect = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 204))
    
    def test5(self):
        input = """a,b,c,d : string = a[1],b+d,{123,4},foo(goo(hoo())) ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    """function declaration"""
    def test6(self):
        input = """
            main: function integer (){}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test7(self):
        input = """ 
            main:function array [2,2] of string (out b: string){
                for(i = -a[b[c["2"]]] , (i+4 > 5) == true, a * -goo()){
                    {{}}
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test8(self):
        input = """
            fact: function void (inherit out x : void){
                
            }
        """
        expect = "Error on line 2 col 49: void"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test9(self):
        input = """
            fact: function integer(a,b: array){
                
            }
        """
        expect = "Error on line 2 col 36: ,"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test10(self):
        input = input = """
            main: function void () {
                x = foo(-{1,2,3});
                while (true) {
                    do
                    while(false);
                }
            }
        """
        expect = "Error on line 6 col 20: while"
        self.assertTrue(TestParser.test(input, expect, 210))

    """ test statement """
    def test11(self):
        input = input = """
            if(i) return 1;
        """
        expect = "Error on line 2 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test12(self):
        input = input = """
        main: function void (){
            if (i) return 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test13(self):
        input = """
            main: function void (){
                x: integer = 1;
                x = x + -foo(b,c,d,e);
                if(x) return 1;
                else return 3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test14(self):
        input = """
        main: function void (inherit out x: string){
            if(true){
                id = (------------id == 21) > 4;
            }
            else {
                if(false){}else{}
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        input = """
            main:function void (){
                if (x) 
                    if(y) return 1; 
                    else return 2;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    
    def test16(self):
        input = """
        inc: function void(out n: integer, delta: integer) inherit abc {
            if(--a[foo(8,{1,3,4}),a[a[a[5]]]]) return;
            else 
                if (_1) return a==2+d; 
                else return true;
        }      
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def test17(self):
        input = """
          fact: function integer (){
              if(if) return 3;
          }  
        """
        expect = "Error on line 3 col 17: if"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        input = """
            fibo: function integer (n: integer){
                if (n==1) return 1;
                if (n==0) return 0;
                return n + fibo(n-1);
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test19(self):
        input = """
        main: function void (){
            while(true)
                do{
                    a[-"a"]=b>d;
                }while(1);
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self):
        input = """
            main: function string(out inherit x: array [1] of string){}  
        """
        expect = "Error on line 2 col 38: inherit"
        self.assertTrue(TestParser.test(input, expect, 220))


    def test_21(self):
        input = """
        a:integer=1;
          fact: function integer (){
              do {x = {1,2,3,01} ;}
              while (true);
            }  
        """
        expect = "Error on line 4 col 30: 1"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_22(self):
        input = """
        a:integer;
          fact: function integer (){
              a = 1;
              do {x = {1,2,3,1} ;}
              while (true);
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_23(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              a = 1;
              do {x = {1,2,3,1} ;}
              while (true);
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_24(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              {}
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_25(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_26(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              {
                  {  
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_27(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              {
                  {  
                  return {12_3.e+5,123,"he ask me \\"",true, a[1,2],foo()};
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_28(self):
        input = """
        a:integer = "he aske me\n";
          fact: function integer (){
              {
                  {  
                  return {12_3.e+5,123,"he ask me \\"",true, a[1,2],foo()};
                  }
              }
            }  
        """
        expect = "he aske me"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_29(self):
        input = """
        a:integer = truee;
          fact: function integer (){
              {
                  {  
                  return {12_3.e+5,123,"he ask me \\"",true, a[1,2],foo()};
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_30(self):
        input = """
        a:integer = truee;
          fact: function integer (){
              {
                  {  
                  return ;
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))  
    '''
    def test_31(self):
        input = """
        a:integer = truee;
          fact: function integer (){
              {
                  {  

                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231)) 
    def test_32(self):
        input = """
        a:integer = truee;
          fact: function integer (){
              {
                  {  
                  if(x==2) return;
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232)) 
    def test_33(self):
        input = """
        a:integer = 1 ;
          fact: function integer (){
              {
                  {  
                  if(x==2) return;
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233)) 
    def test_34(self):
        input = """
        a,b,c:integer =1 ;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "Error on line 2 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_35(self):
        input = """
        a,b,c:integer =1,a[2[3]],3;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "Error on line 2 col 28: ["
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_36(self):
        input = """
        a,b,c:integer =1,a[a[3]],3;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_37(self):
        input = """
        a,b,c:integer =1,a[a[3]],3;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_38(self):
        input = """
        a,b,c:array [2_1_2,3_1] of string;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_39(self):
        input = """
        a,b,c:array [2_1_2,3_] of string;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "Error on line 2 col 28: _"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_40(self):
        input = """
        a,b,c:array [2_1_2,3] of string; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_41(self):
        input = """
        a,b,c: auto; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_42(self):
        input = """
        a,b,c: void; 
        """
        expect = "Error on line 2 col 15: void"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_43(self):
        input = """
        _a_,b,c: string ; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_44(self):
        input = """
        _a_,0b,c: string ; 
        """
        expect = "Error on line 2 col 12: 0"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_45(self):
        input = """
        _a_,_0b,c: boolean ; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_46(self):
        input = """
        _a_,_0b,c: float; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_47(self):
        input = """
        _a_,_0b,c: float; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_48(self):
        input = """
        /* 0a:integer;
        */
        a: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_49(self):
        input = """
        // 0a:integer;
        
        a: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_50(self):
        input = """
        // 0a:integer;
        
        a: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_51(self):
        input = """
        // 0a:integer;
        
        {}
        """
        expect = "Error on line 4 col 8: {"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_52(self):
        input = """
        a:integer = a[1];
          fact: function integer (inherit out x:integer){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_53(self):
        input = """
        a:integer = a[1];
          fact: function integer (inherit x:integer){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_54(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:integer){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_55(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:void){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "Error on line 3 col 40: void"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_55(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:void){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "Error on line 3 col 40: void"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_56(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              if(x==2) a=b[2,2==3];
              if(x>3) a=2;
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_57(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              if(x==2) a=b[2,foo(2)];
              if(x>3) a=2;
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_58(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              if(x==2) a=b[2,foo(x,2),c[1]];
              if(x>3) a=2;
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_59(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              if(x==2) a=b[2,foo(x,2),c[1]];
              if(x>3) a=2;
              a= 2==3;
              a= (2+3);
              while(x<2)x=x+1;
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test_60(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              for (i = 1, i < 10, i + 1) {
                writeInt(i);
                {
                    ;
                }
            }
            }  
        """
        expect = "Error on line 7 col 20: ;"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_61(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              for (i = 1, i < 10, i + 1) {
                writeInt(i);
                {
                    ;
                }
            }
            }  
        """
        expect = "Error on line 7 col 20: ;"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_62(self):
        input = """
        a:integer = a[1];
        return ;
          fact: function integer (out x:string){
              for (i = 1, i < 10, i + 1) {
                writeInt(i);
                {
                    ;
                }
            }
            }  
        """
        expect = "Error on line 3 col 8: return"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_63(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              {
                  
              
            } 
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_66(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
    def test_67(self):
        input = """
        a:integer = a[1,{1,2,3}];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_68(self):
        input = """
        a:integer = a[1,/*111_*/2];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
    def test_69(self):
        input = """
        a:integer = a[1,/*111_*/2_];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 33: _"
        self.assertTrue(TestParser.test(input, expect, 269))
    def test_70(self):
        input = """
        a:integer = a[1,2/*111_*///aa];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 3 col 10: fact"
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_71(self):
        input = """
        a:integer = a[1,foo(1,{1,2,3}),boolean];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 39: boolean"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test_72(self):
        input = """
        a:integer = a[1,foo(1,{1,2,3}),integer];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 39: integer"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_73(self):
        input = """
        a:integer = a[1,foo(1,{1,2,3}),float];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 39: float"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_74(self):
        input = """
        a:integer = aa :: bb;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_75(self):
        input = """
        a:integer = aa :: bb :: cc;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 29: ::"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_76(self):
        input = """
a:integer = aa :: (bb :: cc);
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_77(self):
        input = """
        a:integer = (aa == bb) >= cc;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_78(self):
        input = """
        a:integer = aa == bb >= cc;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 29: >="
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_79(self):
        input = """
        a:integer = (aa && bb)&&cc;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    def test_80(self):
        input = """
        a:integer = 1 && (bb&&cc);
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_81(self):
        input = """
        a:integer = {foo(1,2),2};
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_82(self):
        input = """
        a : boolean = true;
                add: function void(i: float) {
                    return i;
                }
                inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                    n = n + delta + hallo;
                    n = n - delta - hallo;
                    n = n * delta * hallo;
                    /* multiple
                        line
                        comment
                    */
                    n = a[1, a[1, a[1,2]]]; // n[1,2] = 2 => n = a[1,2];
                    return n;
        """
        expect = "Error on line 16 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_83(self):
        input = """
        a : boolean = true;
                add: function void(i: float) {
                    return i;
                }
                inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                    n = n + delta + hallo;
                    n = n - delta - hallo;
                    n = n * delta * hallo;
                    /* multiple
                        line
                        comment
                    */
                    n = a[1, a[1, a[1,2]]]; // n[1,2] = 2 => n = a[1,2];
                    return n;
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_84(self):
        input = """
        a : boolean = true;
                add: function void(i: float) {
                    return i;
                }
                inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                    n = n + delta + hallo;
                    return ;
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_85(self):
        input = """
        a : boolean = true;
                add: function void(i: float) {
                    return i;
                }
                inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                    n = n + delta + hallo;
                    return ;
                    ;
                    }
        """
        expect = "Error on line 9 col 20: ;"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_290(self):
        input = """
        learningtofly: function integer() {
                for (i = -foo(), i < 10, i :: -2 :: 3E-10) {
                    a = ---a;
                    }
        }
        """
        expect = "Error on line 3 col 49: ::"
        self.assertTrue(TestParser.test(input, expect, 290))
        '''
