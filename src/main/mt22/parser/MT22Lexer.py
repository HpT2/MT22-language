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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("?\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3$\n\3\f\3\16\3\'")
        buf.write("\13\3\3\3\3\3\3\4\3\4\7\4-\n\4\f\4\16\4\60\13\4\3\5\6")
        buf.write("\5\63\n\5\r\5\16\5\64\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\27\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\6\4\2")
        buf.write("\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"")
        buf.write("\"\2B\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5")
        buf.write("\37\3\2\2\2\7*\3\2\2\2\t\62\3\2\2\2\138\3\2\2\2\r;\3\2")
        buf.write("\2\2\17=\3\2\2\2\21\22\7\61\2\2\22\23\7,\2\2\23\27\3\2")
        buf.write("\2\2\24\26\13\2\2\2\25\24\3\2\2\2\26\31\3\2\2\2\27\30")
        buf.write("\3\2\2\2\27\25\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32")
        buf.write("\33\7,\2\2\33\34\7\61\2\2\34\35\3\2\2\2\35\36\b\2\2\2")
        buf.write("\36\4\3\2\2\2\37 \7\61\2\2 !\7\61\2\2!%\3\2\2\2\"$\n\2")
        buf.write("\2\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2")
        buf.write("\2\'%\3\2\2\2()\b\3\2\2)\6\3\2\2\2*.\t\3\2\2+-\t\4\2\2")
        buf.write(",+\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\b\3\2\2\2")
        buf.write("\60.\3\2\2\2\61\63\t\5\2\2\62\61\3\2\2\2\63\64\3\2\2\2")
        buf.write("\64\62\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\b\5\2")
        buf.write("\2\67\n\3\2\2\289\13\2\2\29:\b\6\3\2:\f\3\2\2\2;<\13\2")
        buf.write("\2\2<\16\3\2\2\2=>\13\2\2\2>\20\3\2\2\2\7\2\27%.\64\4")
        buf.write("\b\2\2\3\6\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    LINE_COMMENT = 2
    ID = 3
    WS = 4
    ERROR_CHAR = 5
    UNCLOSE_STRING = 6
    ILLEGAL_ESCAPE = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LINE_COMMENT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "LINE_COMMENT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[4] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


