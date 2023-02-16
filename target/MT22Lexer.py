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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u00e4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\7\27\u00bb\n\27\f\27\16\27\u00be")
        buf.write("\13\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\7")
        buf.write("\30\u00c9\n\30\f\30\16\30\u00cc\13\30\3\30\3\30\3\31\3")
        buf.write("\31\7\31\u00d2\n\31\f\31\16\31\u00d5\13\31\3\32\6\32\u00d8")
        buf.write("\n\32\r\32\16\32\u00d9\3\32\3\32\3\33\3\33\3\33\3\34\3")
        buf.write("\34\3\35\3\35\3\u00bc\2\36\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write("\3\2\6\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\2\u00e7\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\3;\3\2\2\2\5@\3")
        buf.write("\2\2\2\7F\3\2\2\2\tN\3\2\2\2\13Q\3\2\2\2\rV\3\2\2\2\17")
        buf.write("\\\3\2\2\2\21b\3\2\2\2\23f\3\2\2\2\25o\3\2\2\2\27r\3\2")
        buf.write("\2\2\31z\3\2\2\2\33\u0081\3\2\2\2\35\u0088\3\2\2\2\37")
        buf.write("\u008d\3\2\2\2!\u0093\3\2\2\2#\u0098\3\2\2\2%\u009c\3")
        buf.write("\2\2\2\'\u00a5\3\2\2\2)\u00a8\3\2\2\2+\u00b0\3\2\2\2-")
        buf.write("\u00b6\3\2\2\2/\u00c4\3\2\2\2\61\u00cf\3\2\2\2\63\u00d7")
        buf.write("\3\2\2\2\65\u00dd\3\2\2\2\67\u00e0\3\2\2\29\u00e2\3\2")
        buf.write("\2\2;<\7c\2\2<=\7w\2\2=>\7v\2\2>?\7q\2\2?\4\3\2\2\2@A")
        buf.write("\7d\2\2AB\7t\2\2BC\7g\2\2CD\7c\2\2DE\7m\2\2E\6\3\2\2\2")
        buf.write("FG\7d\2\2GH\7q\2\2HI\7q\2\2IJ\7n\2\2JK\7g\2\2KL\7c\2\2")
        buf.write("LM\7p\2\2M\b\3\2\2\2NO\7f\2\2OP\7q\2\2P\n\3\2\2\2QR\7")
        buf.write("g\2\2RS\7n\2\2ST\7u\2\2TU\7g\2\2U\f\3\2\2\2VW\7h\2\2W")
        buf.write("X\7c\2\2XY\7n\2\2YZ\7u\2\2Z[\7g\2\2[\16\3\2\2\2\\]\7h")
        buf.write("\2\2]^\7n\2\2^_\7q\2\2_`\7c\2\2`a\7v\2\2a\20\3\2\2\2b")
        buf.write("c\7h\2\2cd\7q\2\2de\7t\2\2e\22\3\2\2\2fg\7h\2\2gh\7w\2")
        buf.write("\2hi\7p\2\2ij\7e\2\2jk\7v\2\2kl\7k\2\2lm\7q\2\2mn\7p\2")
        buf.write("\2n\24\3\2\2\2op\7k\2\2pq\7h\2\2q\26\3\2\2\2rs\7k\2\2")
        buf.write("st\7p\2\2tu\7v\2\2uv\7g\2\2vw\7i\2\2wx\7g\2\2xy\7t\2\2")
        buf.write("y\30\3\2\2\2z{\7t\2\2{|\7g\2\2|}\7v\2\2}~\7w\2\2~\177")
        buf.write("\7t\2\2\177\u0080\7p\2\2\u0080\32\3\2\2\2\u0081\u0082")
        buf.write("\7u\2\2\u0082\u0083\7v\2\2\u0083\u0084\7t\2\2\u0084\u0085")
        buf.write("\7k\2\2\u0085\u0086\7p\2\2\u0086\u0087\7i\2\2\u0087\34")
        buf.write("\3\2\2\2\u0088\u0089\7v\2\2\u0089\u008a\7t\2\2\u008a\u008b")
        buf.write("\7w\2\2\u008b\u008c\7g\2\2\u008c\36\3\2\2\2\u008d\u008e")
        buf.write("\7y\2\2\u008e\u008f\7j\2\2\u008f\u0090\7k\2\2\u0090\u0091")
        buf.write("\7n\2\2\u0091\u0092\7g\2\2\u0092 \3\2\2\2\u0093\u0094")
        buf.write("\7x\2\2\u0094\u0095\7q\2\2\u0095\u0096\7k\2\2\u0096\u0097")
        buf.write("\7f\2\2\u0097\"\3\2\2\2\u0098\u0099\7q\2\2\u0099\u009a")
        buf.write("\7w\2\2\u009a\u009b\7v\2\2\u009b$\3\2\2\2\u009c\u009d")
        buf.write("\7e\2\2\u009d\u009e\7q\2\2\u009e\u009f\7p\2\2\u009f\u00a0")
        buf.write("\7v\2\2\u00a0\u00a1\7k\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3")
        buf.write("\7w\2\2\u00a3\u00a4\7g\2\2\u00a4&\3\2\2\2\u00a5\u00a6")
        buf.write("\7q\2\2\u00a6\u00a7\7h\2\2\u00a7(\3\2\2\2\u00a8\u00a9")
        buf.write("\7k\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7j\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af*\3\2\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7t\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5")
        buf.write("\7{\2\2\u00b5,\3\2\2\2\u00b6\u00b7\7\61\2\2\u00b7\u00b8")
        buf.write("\7,\2\2\u00b8\u00bc\3\2\2\2\u00b9\u00bb\13\2\2\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00bc\3")
        buf.write("\2\2\2\u00bf\u00c0\7,\2\2\u00c0\u00c1\7\61\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c3\b\27\2\2\u00c3.\3\2\2\2\u00c4\u00c5")
        buf.write("\7\61\2\2\u00c5\u00c6\7\61\2\2\u00c6\u00ca\3\2\2\2\u00c7")
        buf.write("\u00c9\n\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2")
        buf.write("\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cd\3")
        buf.write("\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\b\30\2\2\u00ce")
        buf.write("\60\3\2\2\2\u00cf\u00d3\t\3\2\2\u00d0\u00d2\t\4\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\62\3\2\2\2\u00d5\u00d3\3\2")
        buf.write("\2\2\u00d6\u00d8\t\5\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00dc\b\32\2\2\u00dc\64\3\2\2\2\u00dd")
        buf.write("\u00de\13\2\2\2\u00de\u00df\b\33\3\2\u00df\66\3\2\2\2")
        buf.write("\u00e0\u00e1\13\2\2\2\u00e18\3\2\2\2\u00e2\u00e3\13\2")
        buf.write("\2\2\u00e3:\3\2\2\2\7\2\u00bc\u00ca\u00d3\u00d9\4\b\2")
        buf.write("\2\3\33\2")
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
    COMMENT = 22
    LINE_COMMENT = 23
    ID = 24
    WS = 25
    ERROR_CHAR = 26
    UNCLOSE_STRING = 27
    ILLEGAL_ESCAPE = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "COMMENT", "LINE_COMMENT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "COMMENT", "LINE_COMMENT", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[25] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


