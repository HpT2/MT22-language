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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u0189\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\7")
        buf.write("\61\u0134\n\61\f\61\16\61\u0137\13\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\7\62\u0142\n\62\f\62\16\62")
        buf.write("\u0145\13\62\3\62\3\62\3\63\3\63\7\63\u014b\n\63\f\63")
        buf.write("\16\63\u014e\13\63\3\64\3\64\3\64\3\65\3\65\5\65\u0155")
        buf.write("\n\65\3\65\5\65\u0158\n\65\3\65\3\65\3\66\3\66\3\66\5")
        buf.write("\66\u015f\n\66\3\66\6\66\u0162\n\66\r\66\16\66\u0163\7")
        buf.write("\66\u0166\n\66\f\66\16\66\u0169\13\66\5\66\u016b\n\66")
        buf.write("\3\67\3\67\6\67\u016f\n\67\r\67\16\67\u0170\38\38\58\u0175")
        buf.write("\n8\38\68\u0178\n8\r8\168\u0179\39\69\u017d\n9\r9\169")
        buf.write("\u017e\39\39\3:\3:\3:\3;\3;\3<\3<\3\u0135\2=\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2q\67s8u9w:\3")
        buf.write("\2\n\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2\u0192\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\3y\3\2\2\2\5~\3\2\2\2\7\u0084\3\2\2\2\t\u008c")
        buf.write("\3\2\2\2\13\u008f\3\2\2\2\r\u0094\3\2\2\2\17\u009a\3\2")
        buf.write("\2\2\21\u00a0\3\2\2\2\23\u00a4\3\2\2\2\25\u00ad\3\2\2")
        buf.write("\2\27\u00b0\3\2\2\2\31\u00b8\3\2\2\2\33\u00bf\3\2\2\2")
        buf.write("\35\u00c6\3\2\2\2\37\u00cb\3\2\2\2!\u00d1\3\2\2\2#\u00d6")
        buf.write("\3\2\2\2%\u00da\3\2\2\2\'\u00e3\3\2\2\2)\u00e6\3\2\2\2")
        buf.write("+\u00ee\3\2\2\2-\u00f4\3\2\2\2/\u00f6\3\2\2\2\61\u00f8")
        buf.write("\3\2\2\2\63\u00fa\3\2\2\2\65\u00fc\3\2\2\2\67\u00fe\3")
        buf.write("\2\2\29\u0100\3\2\2\2;\u0103\3\2\2\2=\u0106\3\2\2\2?\u0109")
        buf.write("\3\2\2\2A\u010c\3\2\2\2C\u010e\3\2\2\2E\u0111\3\2\2\2")
        buf.write("G\u0113\3\2\2\2I\u0116\3\2\2\2K\u0119\3\2\2\2M\u011b\3")
        buf.write("\2\2\2O\u011d\3\2\2\2Q\u011f\3\2\2\2S\u0121\3\2\2\2U\u0123")
        buf.write("\3\2\2\2W\u0125\3\2\2\2Y\u0127\3\2\2\2[\u0129\3\2\2\2")
        buf.write("]\u012b\3\2\2\2_\u012d\3\2\2\2a\u012f\3\2\2\2c\u013d\3")
        buf.write("\2\2\2e\u0148\3\2\2\2g\u014f\3\2\2\2i\u0152\3\2\2\2k\u016a")
        buf.write("\3\2\2\2m\u016c\3\2\2\2o\u0172\3\2\2\2q\u017c\3\2\2\2")
        buf.write("s\u0182\3\2\2\2u\u0185\3\2\2\2w\u0187\3\2\2\2yz\7c\2\2")
        buf.write("z{\7w\2\2{|\7v\2\2|}\7q\2\2}\4\3\2\2\2~\177\7d\2\2\177")
        buf.write("\u0080\7t\2\2\u0080\u0081\7g\2\2\u0081\u0082\7c\2\2\u0082")
        buf.write("\u0083\7m\2\2\u0083\6\3\2\2\2\u0084\u0085\7d\2\2\u0085")
        buf.write("\u0086\7q\2\2\u0086\u0087\7q\2\2\u0087\u0088\7n\2\2\u0088")
        buf.write("\u0089\7g\2\2\u0089\u008a\7c\2\2\u008a\u008b\7p\2\2\u008b")
        buf.write("\b\3\2\2\2\u008c\u008d\7f\2\2\u008d\u008e\7q\2\2\u008e")
        buf.write("\n\3\2\2\2\u008f\u0090\7g\2\2\u0090\u0091\7n\2\2\u0091")
        buf.write("\u0092\7u\2\2\u0092\u0093\7g\2\2\u0093\f\3\2\2\2\u0094")
        buf.write("\u0095\7h\2\2\u0095\u0096\7c\2\2\u0096\u0097\7n\2\2\u0097")
        buf.write("\u0098\7u\2\2\u0098\u0099\7g\2\2\u0099\16\3\2\2\2\u009a")
        buf.write("\u009b\7h\2\2\u009b\u009c\7n\2\2\u009c\u009d\7q\2\2\u009d")
        buf.write("\u009e\7c\2\2\u009e\u009f\7v\2\2\u009f\20\3\2\2\2\u00a0")
        buf.write("\u00a1\7h\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7t\2\2\u00a3")
        buf.write("\22\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6")
        buf.write("\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\u00a9\7v\2\2\u00a9")
        buf.write("\u00aa\7k\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7p\2\2\u00ac")
        buf.write("\24\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7h\2\2\u00af")
        buf.write("\26\3\2\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7p\2\2\u00b2")
        buf.write("\u00b3\7v\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7i\2\2\u00b5")
        buf.write("\u00b6\7g\2\2\u00b6\u00b7\7t\2\2\u00b7\30\3\2\2\2\u00b8")
        buf.write("\u00b9\7t\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7v\2\2\u00bb")
        buf.write("\u00bc\7w\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7p\2\2\u00be")
        buf.write("\32\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1\7v\2\2\u00c1")
        buf.write("\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7p\2\2\u00c4")
        buf.write("\u00c5\7i\2\2\u00c5\34\3\2\2\2\u00c6\u00c7\7v\2\2\u00c7")
        buf.write("\u00c8\7t\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\36\3\2\2\2\u00cb\u00cc\7y\2\2\u00cc\u00cd\7j\2\2\u00cd")
        buf.write("\u00ce\7k\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7g\2\2\u00d0")
        buf.write(" \3\2\2\2\u00d1\u00d2\7x\2\2\u00d2\u00d3\7q\2\2\u00d3")
        buf.write("\u00d4\7k\2\2\u00d4\u00d5\7f\2\2\u00d5\"\3\2\2\2\u00d6")
        buf.write("\u00d7\7q\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9\7v\2\2\u00d9")
        buf.write("$\3\2\2\2\u00da\u00db\7e\2\2\u00db\u00dc\7q\2\2\u00dc")
        buf.write("\u00dd\7p\2\2\u00dd\u00de\7v\2\2\u00de\u00df\7k\2\2\u00df")
        buf.write("\u00e0\7p\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2\7g\2\2\u00e2")
        buf.write("&\3\2\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7h\2\2\u00e5")
        buf.write("(\3\2\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7p\2\2\u00e8")
        buf.write("\u00e9\7j\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7t\2\2\u00eb")
        buf.write("\u00ec\7k\2\2\u00ec\u00ed\7v\2\2\u00ed*\3\2\2\2\u00ee")
        buf.write("\u00ef\7c\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7t\2\2\u00f1")
        buf.write("\u00f2\7c\2\2\u00f2\u00f3\7{\2\2\u00f3,\3\2\2\2\u00f4")
        buf.write("\u00f5\7-\2\2\u00f5.\3\2\2\2\u00f6\u00f7\7/\2\2\u00f7")
        buf.write("\60\3\2\2\2\u00f8\u00f9\7,\2\2\u00f9\62\3\2\2\2\u00fa")
        buf.write("\u00fb\7\61\2\2\u00fb\64\3\2\2\2\u00fc\u00fd\7\'\2\2\u00fd")
        buf.write("\66\3\2\2\2\u00fe\u00ff\7#\2\2\u00ff8\3\2\2\2\u0100\u0101")
        buf.write("\7(\2\2\u0101\u0102\7(\2\2\u0102:\3\2\2\2\u0103\u0104")
        buf.write("\7~\2\2\u0104\u0105\7~\2\2\u0105<\3\2\2\2\u0106\u0107")
        buf.write("\7?\2\2\u0107\u0108\7?\2\2\u0108>\3\2\2\2\u0109\u010a")
        buf.write("\7#\2\2\u010a\u010b\7?\2\2\u010b@\3\2\2\2\u010c\u010d")
        buf.write("\7>\2\2\u010dB\3\2\2\2\u010e\u010f\7>\2\2\u010f\u0110")
        buf.write("\7?\2\2\u0110D\3\2\2\2\u0111\u0112\7@\2\2\u0112F\3\2\2")
        buf.write("\2\u0113\u0114\7@\2\2\u0114\u0115\7?\2\2\u0115H\3\2\2")
        buf.write("\2\u0116\u0117\7<\2\2\u0117\u0118\7<\2\2\u0118J\3\2\2")
        buf.write("\2\u0119\u011a\7*\2\2\u011aL\3\2\2\2\u011b\u011c\7+\2")
        buf.write("\2\u011cN\3\2\2\2\u011d\u011e\7]\2\2\u011eP\3\2\2\2\u011f")
        buf.write("\u0120\7_\2\2\u0120R\3\2\2\2\u0121\u0122\7\60\2\2\u0122")
        buf.write("T\3\2\2\2\u0123\u0124\7.\2\2\u0124V\3\2\2\2\u0125\u0126")
        buf.write("\7=\2\2\u0126X\3\2\2\2\u0127\u0128\7<\2\2\u0128Z\3\2\2")
        buf.write("\2\u0129\u012a\7}\2\2\u012a\\\3\2\2\2\u012b\u012c\7\177")
        buf.write("\2\2\u012c^\3\2\2\2\u012d\u012e\7?\2\2\u012e`\3\2\2\2")
        buf.write("\u012f\u0130\7\61\2\2\u0130\u0131\7,\2\2\u0131\u0135\3")
        buf.write("\2\2\2\u0132\u0134\13\2\2\2\u0133\u0132\3\2\2\2\u0134")
        buf.write("\u0137\3\2\2\2\u0135\u0136\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0136\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139\7")
        buf.write(",\2\2\u0139\u013a\7\61\2\2\u013a\u013b\3\2\2\2\u013b\u013c")
        buf.write("\b\61\2\2\u013cb\3\2\2\2\u013d\u013e\7\61\2\2\u013e\u013f")
        buf.write("\7\61\2\2\u013f\u0143\3\2\2\2\u0140\u0142\n\2\2\2\u0141")
        buf.write("\u0140\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0143\3")
        buf.write("\2\2\2\u0146\u0147\b\62\2\2\u0147d\3\2\2\2\u0148\u014c")
        buf.write("\t\3\2\2\u0149\u014b\t\4\2\2\u014a\u0149\3\2\2\2\u014b")
        buf.write("\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2")
        buf.write("\u014df\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0150\5k\66")
        buf.write("\2\u0150\u0151\b\64\3\2\u0151h\3\2\2\2\u0152\u0154\5k")
        buf.write("\66\2\u0153\u0155\5m\67\2\u0154\u0153\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0157\3\2\2\2\u0156\u0158\5o8\2\u0157\u0156")
        buf.write("\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("\u015a\b\65\4\2\u015aj\3\2\2\2\u015b\u016b\7\62\2\2\u015c")
        buf.write("\u0167\t\5\2\2\u015d\u015f\7a\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015e\u015f\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u0162\t")
        buf.write("\6\2\2\u0161\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0161")
        buf.write("\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165")
        buf.write("\u015e\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3")
        buf.write("\2\2\2\u016a\u015b\3\2\2\2\u016a\u015c\3\2\2\2\u016bl")
        buf.write("\3\2\2\2\u016c\u016e\7\60\2\2\u016d\u016f\t\6\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171n\3\2\2\2\u0172\u0174\t\7\2")
        buf.write("\2\u0173\u0175\t\b\2\2\u0174\u0173\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0178\t\6\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017ap\3\2\2\2\u017b\u017d\t\t\2")
        buf.write("\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\b9\2\2\u0181r\3\2\2\2\u0182\u0183\13\2\2\2\u0183")
        buf.write("\u0184\b:\5\2\u0184t\3\2\2\2\u0185\u0186\13\2\2\2\u0186")
        buf.write("v\3\2\2\2\u0187\u0188\13\2\2\2\u0188x\3\2\2\2\20\2\u0135")
        buf.write("\u0143\u014c\u0154\u0157\u015e\u0163\u0167\u016a\u0170")
        buf.write("\u0174\u0179\u017e\6\b\2\2\3\64\2\3\65\3\3:\4")
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
    INT_TYPE = 51
    FLOAT_TYPE = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

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
            "ID", "INT_TYPE", "FLOAT_TYPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODULO", 
                  "LOGICNOT", "AND", "OR", "EQ", "NOTEQ", "LESS", "LESSOREQ", 
                  "MORE_", "MOREOREQ", "DBLCOL", "LP", "RP", "LSB", "RSB", 
                  "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "ASSIGN", 
                  "COMMENT", "LINE_COMMENT", "ID", "INT_TYPE", "FLOAT_TYPE", 
                  "INTPART", "DECIMAL", "EXPONENT", "WS", "ERROR_CHAR", 
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
            actions[50] = self.INT_TYPE_action 
            actions[51] = self.FLOAT_TYPE_action 
            actions[56] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOAT_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


