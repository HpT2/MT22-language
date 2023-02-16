# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


#2012385
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u0153\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\7\61\u012a\n\61\f\61\16\61\u012d\13\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u0138")
        buf.write("\n\62\f\62\16\62\u013b\13\62\3\62\3\62\3\63\3\63\7\63")
        buf.write("\u0141\n\63\f\63\16\63\u0144\13\63\3\64\6\64\u0147\n\64")
        buf.write("\r\64\16\64\u0148\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3")
        buf.write("\67\3\67\3\u012b\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8\3\2\6\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C")
        buf.write("\\aac|\5\2\13\f\17\17\"\"\2\u0156\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\3o\3\2\2\2\5t\3\2\2\2\7z\3\2\2\2")
        buf.write("\t\u0082\3\2\2\2\13\u0085\3\2\2\2\r\u008a\3\2\2\2\17\u0090")
        buf.write("\3\2\2\2\21\u0096\3\2\2\2\23\u009a\3\2\2\2\25\u00a3\3")
        buf.write("\2\2\2\27\u00a6\3\2\2\2\31\u00ae\3\2\2\2\33\u00b5\3\2")
        buf.write("\2\2\35\u00bc\3\2\2\2\37\u00c1\3\2\2\2!\u00c7\3\2\2\2")
        buf.write("#\u00cc\3\2\2\2%\u00d0\3\2\2\2\'\u00d9\3\2\2\2)\u00dc")
        buf.write("\3\2\2\2+\u00e4\3\2\2\2-\u00ea\3\2\2\2/\u00ec\3\2\2\2")
        buf.write("\61\u00ee\3\2\2\2\63\u00f0\3\2\2\2\65\u00f2\3\2\2\2\67")
        buf.write("\u00f4\3\2\2\29\u00f6\3\2\2\2;\u00f9\3\2\2\2=\u00fc\3")
        buf.write("\2\2\2?\u00ff\3\2\2\2A\u0102\3\2\2\2C\u0104\3\2\2\2E\u0107")
        buf.write("\3\2\2\2G\u0109\3\2\2\2I\u010c\3\2\2\2K\u010f\3\2\2\2")
        buf.write("M\u0111\3\2\2\2O\u0113\3\2\2\2Q\u0115\3\2\2\2S\u0117\3")
        buf.write("\2\2\2U\u0119\3\2\2\2W\u011b\3\2\2\2Y\u011d\3\2\2\2[\u011f")
        buf.write("\3\2\2\2]\u0121\3\2\2\2_\u0123\3\2\2\2a\u0125\3\2\2\2")
        buf.write("c\u0133\3\2\2\2e\u013e\3\2\2\2g\u0146\3\2\2\2i\u014c\3")
        buf.write("\2\2\2k\u014f\3\2\2\2m\u0151\3\2\2\2op\7c\2\2pq\7w\2\2")
        buf.write("qr\7v\2\2rs\7q\2\2s\4\3\2\2\2tu\7d\2\2uv\7t\2\2vw\7g\2")
        buf.write("\2wx\7c\2\2xy\7m\2\2y\6\3\2\2\2z{\7d\2\2{|\7q\2\2|}\7")
        buf.write("q\2\2}~\7n\2\2~\177\7g\2\2\177\u0080\7c\2\2\u0080\u0081")
        buf.write("\7p\2\2\u0081\b\3\2\2\2\u0082\u0083\7f\2\2\u0083\u0084")
        buf.write("\7q\2\2\u0084\n\3\2\2\2\u0085\u0086\7g\2\2\u0086\u0087")
        buf.write("\7n\2\2\u0087\u0088\7u\2\2\u0088\u0089\7g\2\2\u0089\f")
        buf.write("\3\2\2\2\u008a\u008b\7h\2\2\u008b\u008c\7c\2\2\u008c\u008d")
        buf.write("\7n\2\2\u008d\u008e\7u\2\2\u008e\u008f\7g\2\2\u008f\16")
        buf.write("\3\2\2\2\u0090\u0091\7h\2\2\u0091\u0092\7n\2\2\u0092\u0093")
        buf.write("\7q\2\2\u0093\u0094\7c\2\2\u0094\u0095\7v\2\2\u0095\20")
        buf.write("\3\2\2\2\u0096\u0097\7h\2\2\u0097\u0098\7q\2\2\u0098\u0099")
        buf.write("\7t\2\2\u0099\22\3\2\2\2\u009a\u009b\7h\2\2\u009b\u009c")
        buf.write("\7w\2\2\u009c\u009d\7p\2\2\u009d\u009e\7e\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2\24\3\2\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7h\2\2\u00a5\26\3\2\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8")
        buf.write("\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab")
        buf.write("\7i\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7t\2\2\u00ad\30")
        buf.write("\3\2\2\2\u00ae\u00af\7t\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4")
        buf.write("\7p\2\2\u00b4\32\3\2\2\2\u00b5\u00b6\7u\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba")
        buf.write("\7p\2\2\u00ba\u00bb\7i\2\2\u00bb\34\3\2\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\36\3\2\2\2\u00c1\u00c2\7y\2\2\u00c2\u00c3")
        buf.write("\7j\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7n\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6 \3\2\2\2\u00c7\u00c8\7x\2\2\u00c8\u00c9")
        buf.write("\7q\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7f\2\2\u00cb\"")
        buf.write("\3\2\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf$\3\2\2\2\u00d0\u00d1\7e\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7w\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8&\3\2\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7h\2\2\u00db(\3\2\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\u00df\7j\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7v\2\2\u00e3*\3")
        buf.write("\2\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7")
        buf.write("\7t\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7{\2\2\u00e9,\3")
        buf.write("\2\2\2\u00ea\u00eb\7-\2\2\u00eb.\3\2\2\2\u00ec\u00ed\7")
        buf.write("/\2\2\u00ed\60\3\2\2\2\u00ee\u00ef\7,\2\2\u00ef\62\3\2")
        buf.write("\2\2\u00f0\u00f1\7\61\2\2\u00f1\64\3\2\2\2\u00f2\u00f3")
        buf.write("\7\'\2\2\u00f3\66\3\2\2\2\u00f4\u00f5\7#\2\2\u00f58\3")
        buf.write("\2\2\2\u00f6\u00f7\7(\2\2\u00f7\u00f8\7(\2\2\u00f8:\3")
        buf.write("\2\2\2\u00f9\u00fa\7~\2\2\u00fa\u00fb\7~\2\2\u00fb<\3")
        buf.write("\2\2\2\u00fc\u00fd\7?\2\2\u00fd\u00fe\7?\2\2\u00fe>\3")
        buf.write("\2\2\2\u00ff\u0100\7#\2\2\u0100\u0101\7?\2\2\u0101@\3")
        buf.write("\2\2\2\u0102\u0103\7>\2\2\u0103B\3\2\2\2\u0104\u0105\7")
        buf.write(">\2\2\u0105\u0106\7?\2\2\u0106D\3\2\2\2\u0107\u0108\7")
        buf.write("@\2\2\u0108F\3\2\2\2\u0109\u010a\7@\2\2\u010a\u010b\7")
        buf.write("?\2\2\u010bH\3\2\2\2\u010c\u010d\7<\2\2\u010d\u010e\7")
        buf.write("<\2\2\u010eJ\3\2\2\2\u010f\u0110\7*\2\2\u0110L\3\2\2\2")
        buf.write("\u0111\u0112\7+\2\2\u0112N\3\2\2\2\u0113\u0114\7]\2\2")
        buf.write("\u0114P\3\2\2\2\u0115\u0116\7_\2\2\u0116R\3\2\2\2\u0117")
        buf.write("\u0118\7\60\2\2\u0118T\3\2\2\2\u0119\u011a\7.\2\2\u011a")
        buf.write("V\3\2\2\2\u011b\u011c\7=\2\2\u011cX\3\2\2\2\u011d\u011e")
        buf.write("\7<\2\2\u011eZ\3\2\2\2\u011f\u0120\7}\2\2\u0120\\\3\2")
        buf.write("\2\2\u0121\u0122\7\177\2\2\u0122^\3\2\2\2\u0123\u0124")
        buf.write("\7?\2\2\u0124`\3\2\2\2\u0125\u0126\7\61\2\2\u0126\u0127")
        buf.write("\7,\2\2\u0127\u012b\3\2\2\2\u0128\u012a\13\2\2\2\u0129")
        buf.write("\u0128\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012b\u0129\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u012b\3")
        buf.write("\2\2\2\u012e\u012f\7,\2\2\u012f\u0130\7\61\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131\u0132\b\61\2\2\u0132b\3\2\2\2\u0133\u0134")
        buf.write("\7\61\2\2\u0134\u0135\7\61\2\2\u0135\u0139\3\2\2\2\u0136")
        buf.write("\u0138\n\2\2\2\u0137\u0136\3\2\2\2\u0138\u013b\3\2\2\2")
        buf.write("\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3")
        buf.write("\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\b\62\2\2\u013d")
        buf.write("d\3\2\2\2\u013e\u0142\t\3\2\2\u013f\u0141\t\4\2\2\u0140")
        buf.write("\u013f\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3\2\2\2")
        buf.write("\u0142\u0143\3\2\2\2\u0143f\3\2\2\2\u0144\u0142\3\2\2")
        buf.write("\2\u0145\u0147\t\5\2\2\u0146\u0145\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014a\u014b\b\64\2\2\u014bh\3\2\2\2\u014c")
        buf.write("\u014d\13\2\2\2\u014d\u014e\b\65\3\2\u014ej\3\2\2\2\u014f")
        buf.write("\u0150\13\2\2\2\u0150l\3\2\2\2\u0151\u0152\13\2\2\2\u0152")
        buf.write("n\3\2\2\2\7\2\u012b\u0139\u0142\u0148\4\b\2\2\3\65\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    TRUE = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    ADDOP = 22
    SUBOP = 23
    MULOP = 24
    DIVOP = 25
    MODULO = 26
    LOGICNOT = 27
    AND = 28
    OR = 29
    EQ = 30
    NOTEQ = 31
    LESS = 32
    LESSOREQ = 33
    MORE_ = 34
    MOREOREQ = 35
    DBLCOL = 36
    LP = 37
    RP = 38
    LSB = 39
    RSB = 40
    DOT = 41
    COMMA = 42
    SEMI = 43
    COLON = 44
    LCB = 45
    RCB = 46
    ASSIGN = 47
    COMMENT = 48
    LINE_COMMENT = 49
    ID = 50
    WS = 51
    ERROR_CHAR = 52
    UNCLOSE_STRING = 53
    ILLEGAL_ESCAPE = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODULO", "LOGICNOT", "AND", 
            "OR", "EQ", "NOTEQ", "LESS", "LESSOREQ", "MORE_", "MOREOREQ", 
            "DBLCOL", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", 
            "COLON", "LCB", "RCB", "ASSIGN", "COMMENT", "LINE_COMMENT", 
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODULO", 
                  "LOGICNOT", "AND", "OR", "EQ", "NOTEQ", "LESS", "LESSOREQ", 
                  "MORE_", "MOREOREQ", "DBLCOL", "LP", "RP", "LSB", "RSB", 
                  "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "ASSIGN", 
                  "COMMENT", "LINE_COMMENT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[51] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


