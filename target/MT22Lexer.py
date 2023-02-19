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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u0200\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\7\63\u0154\n\63\f\63\16\63\u0157\13\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\7\64\u0162")
        buf.write("\n\64\f\64\16\64\u0165\13\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\5\65\u016d\n\65\3\65\7\65\u0170\n\65\f\65\16\65")
        buf.write("\u0173\13\65\3\65\3\65\3\65\7\65\u0178\n\65\f\65\16\65")
        buf.write("\u017b\13\65\3\65\3\65\3\65\5\65\u0180\n\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u0187\n\65\3\65\7\65\u018a\n\65\f")
        buf.write("\65\16\65\u018d\13\65\3\65\3\65\3\65\5\65\u0192\n\65\5")
        buf.write("\65\u0194\n\65\3\65\3\65\3\66\3\66\7\66\u019a\n\66\f\66")
        buf.write("\16\66\u019d\13\66\3\67\3\67\3\67\38\38\58\u01a4\n8\3")
        buf.write("8\58\u01a7\n8\38\38\39\39\59\u01ad\n9\39\39\59\u01b1\n")
        buf.write("9\39\69\u01b4\n9\r9\169\u01b5\79\u01b8\n9\f9\169\u01bb")
        buf.write("\139\59\u01bd\n9\3:\3:\6:\u01c1\n:\r:\16:\u01c2\3;\3;")
        buf.write("\5;\u01c7\n;\3;\6;\u01ca\n;\r;\16;\u01cb\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\7<\u01dd\n<\f<\16<\u01e0")
        buf.write("\13<\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\6@\u01ef\n")
        buf.write("@\r@\16@\u01f0\3@\3@\3A\3A\3A\3B\3B\7B\u01fa\nB\fB\16")
        buf.write("B\u01fd\13B\3B\3B\6\u0155\u0171\u0179\u018b\2C\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q\2s\2u\2w:y\2")
        buf.write("{\2}\2\177;\u0081<\u0083=\3\2\f\4\2\f\f\17\17\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\4\2--//\3\2\63;\3\2\62;\4\2GGgg\5\2")
        buf.write("$$))^^\5\2\13\f\17\17\"\"\3\2$$\2\u021a\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2w\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2\2")
        buf.write("\5\u008e\3\2\2\2\7\u0099\3\2\2\2\t\u009e\3\2\2\2\13\u00a4")
        buf.write("\3\2\2\2\r\u00ac\3\2\2\2\17\u00af\3\2\2\2\21\u00b4\3\2")
        buf.write("\2\2\23\u00ba\3\2\2\2\25\u00c0\3\2\2\2\27\u00c4\3\2\2")
        buf.write("\2\31\u00cd\3\2\2\2\33\u00d0\3\2\2\2\35\u00d8\3\2\2\2")
        buf.write("\37\u00df\3\2\2\2!\u00e6\3\2\2\2#\u00eb\3\2\2\2%\u00f1")
        buf.write("\3\2\2\2\'\u00f6\3\2\2\2)\u00fa\3\2\2\2+\u0103\3\2\2\2")
        buf.write("-\u0106\3\2\2\2/\u010e\3\2\2\2\61\u0114\3\2\2\2\63\u0116")
        buf.write("\3\2\2\2\65\u0118\3\2\2\2\67\u011a\3\2\2\29\u011c\3\2")
        buf.write("\2\2;\u011e\3\2\2\2=\u0120\3\2\2\2?\u0123\3\2\2\2A\u0126")
        buf.write("\3\2\2\2C\u0129\3\2\2\2E\u012c\3\2\2\2G\u012e\3\2\2\2")
        buf.write("I\u0131\3\2\2\2K\u0133\3\2\2\2M\u0136\3\2\2\2O\u0139\3")
        buf.write("\2\2\2Q\u013b\3\2\2\2S\u013d\3\2\2\2U\u013f\3\2\2\2W\u0141")
        buf.write("\3\2\2\2Y\u0143\3\2\2\2[\u0145\3\2\2\2]\u0147\3\2\2\2")
        buf.write("_\u0149\3\2\2\2a\u014b\3\2\2\2c\u014d\3\2\2\2e\u014f\3")
        buf.write("\2\2\2g\u015d\3\2\2\2i\u0193\3\2\2\2k\u0197\3\2\2\2m\u019e")
        buf.write("\3\2\2\2o\u01a1\3\2\2\2q\u01bc\3\2\2\2s\u01be\3\2\2\2")
        buf.write("u\u01c4\3\2\2\2w\u01cd\3\2\2\2y\u01e4\3\2\2\2{\u01e7\3")
        buf.write("\2\2\2}\u01ea\3\2\2\2\177\u01ee\3\2\2\2\u0081\u01f4\3")
        buf.write("\2\2\2\u0083\u01f7\3\2\2\2\u0085\u0086\7h\2\2\u0086\u0087")
        buf.write("\7q\2\2\u0087\u0088\7t\2\2\u0088\u0089\7a\2\2\u0089\u008a")
        buf.write("\7u\2\2\u008a\u008b\7v\2\2\u008b\u008c\7o\2\2\u008c\u008d")
        buf.write("\7v\2\2\u008d\4\3\2\2\2\u008e\u008f\7y\2\2\u008f\u0090")
        buf.write("\7j\2\2\u0090\u0091\7k\2\2\u0091\u0092\7n\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\u0094\7a\2\2\u0094\u0095\7u\2\2\u0095\u0096")
        buf.write("\7v\2\2\u0096\u0097\7o\2\2\u0097\u0098\7v\2\2\u0098\6")
        buf.write("\3\2\2\2\u0099\u009a\7c\2\2\u009a\u009b\7w\2\2\u009b\u009c")
        buf.write("\7v\2\2\u009c\u009d\7q\2\2\u009d\b\3\2\2\2\u009e\u009f")
        buf.write("\7d\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2")
        buf.write("\7c\2\2\u00a2\u00a3\7m\2\2\u00a3\n\3\2\2\2\u00a4\u00a5")
        buf.write("\7d\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8")
        buf.write("\7n\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\f\3\2\2\2\u00ac\u00ad\7f\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\16\3\2\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1")
        buf.write("\7n\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3\7g\2\2\u00b3\20")
        buf.write("\3\2\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7")
        buf.write("\7n\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9\7g\2\2\u00b9\22")
        buf.write("\3\2\2\2\u00ba\u00bb\7h\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7v\2\2\u00bf\24")
        buf.write("\3\2\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3")
        buf.write("\7t\2\2\u00c3\26\3\2\2\2\u00c4\u00c5\7h\2\2\u00c5\u00c6")
        buf.write("\7w\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8\7e\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\30\3\2\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7h\2\2\u00cf\32\3\2\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5")
        buf.write("\7i\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7t\2\2\u00d7\34")
        buf.write("\3\2\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7g\2\2\u00da\u00db")
        buf.write("\7v\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\36\3\2\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4\u00e5\7i\2\2\u00e5 \3\2\2\2\u00e6\u00e7")
        buf.write("\7v\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\"\3\2\2\2\u00eb\u00ec\7y\2\2\u00ec\u00ed")
        buf.write("\7j\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0$\3\2\2\2\u00f1\u00f2\7x\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7f\2\2\u00f5&\3")
        buf.write("\2\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9(\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc")
        buf.write("\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7w\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102*\3\2\2\2\u0103\u0104\7q\2\2\u0104\u0105")
        buf.write("\7h\2\2\u0105,\3\2\2\2\u0106\u0107\7k\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7j\2\2\u0109\u010a\7g\2\2\u010a\u010b")
        buf.write("\7t\2\2\u010b\u010c\7k\2\2\u010c\u010d\7v\2\2\u010d.\3")
        buf.write("\2\2\2\u010e\u010f\7c\2\2\u010f\u0110\7t\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111\u0112\7c\2\2\u0112\u0113\7{\2\2\u0113\60")
        buf.write("\3\2\2\2\u0114\u0115\7-\2\2\u0115\62\3\2\2\2\u0116\u0117")
        buf.write("\7/\2\2\u0117\64\3\2\2\2\u0118\u0119\7,\2\2\u0119\66\3")
        buf.write("\2\2\2\u011a\u011b\7\61\2\2\u011b8\3\2\2\2\u011c\u011d")
        buf.write("\7\'\2\2\u011d:\3\2\2\2\u011e\u011f\7#\2\2\u011f<\3\2")
        buf.write("\2\2\u0120\u0121\7(\2\2\u0121\u0122\7(\2\2\u0122>\3\2")
        buf.write("\2\2\u0123\u0124\7~\2\2\u0124\u0125\7~\2\2\u0125@\3\2")
        buf.write("\2\2\u0126\u0127\7?\2\2\u0127\u0128\7?\2\2\u0128B\3\2")
        buf.write("\2\2\u0129\u012a\7#\2\2\u012a\u012b\7?\2\2\u012bD\3\2")
        buf.write("\2\2\u012c\u012d\7>\2\2\u012dF\3\2\2\2\u012e\u012f\7>")
        buf.write("\2\2\u012f\u0130\7?\2\2\u0130H\3\2\2\2\u0131\u0132\7@")
        buf.write("\2\2\u0132J\3\2\2\2\u0133\u0134\7@\2\2\u0134\u0135\7?")
        buf.write("\2\2\u0135L\3\2\2\2\u0136\u0137\7<\2\2\u0137\u0138\7<")
        buf.write("\2\2\u0138N\3\2\2\2\u0139\u013a\7*\2\2\u013aP\3\2\2\2")
        buf.write("\u013b\u013c\7+\2\2\u013cR\3\2\2\2\u013d\u013e\7]\2\2")
        buf.write("\u013eT\3\2\2\2\u013f\u0140\7_\2\2\u0140V\3\2\2\2\u0141")
        buf.write("\u0142\7\60\2\2\u0142X\3\2\2\2\u0143\u0144\7.\2\2\u0144")
        buf.write("Z\3\2\2\2\u0145\u0146\7=\2\2\u0146\\\3\2\2\2\u0147\u0148")
        buf.write("\7<\2\2\u0148^\3\2\2\2\u0149\u014a\7}\2\2\u014a`\3\2\2")
        buf.write("\2\u014b\u014c\7\177\2\2\u014cb\3\2\2\2\u014d\u014e\7")
        buf.write("?\2\2\u014ed\3\2\2\2\u014f\u0150\7\61\2\2\u0150\u0151")
        buf.write("\7,\2\2\u0151\u0155\3\2\2\2\u0152\u0154\13\2\2\2\u0153")
        buf.write("\u0152\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0155\u0153\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0155\3")
        buf.write("\2\2\2\u0158\u0159\7,\2\2\u0159\u015a\7\61\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b\u015c\b\63\2\2\u015cf\3\2\2\2\u015d\u015e")
        buf.write("\7\61\2\2\u015e\u015f\7\61\2\2\u015f\u0163\3\2\2\2\u0160")
        buf.write("\u0162\n\2\2\2\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2")
        buf.write("\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\3")
        buf.write("\2\2\2\u0165\u0163\3\2\2\2\u0166\u0167\b\64\2\2\u0167")
        buf.write("h\3\2\2\2\u0168\u016c\7$\2\2\u0169\u016a\7^\2\2\u016a")
        buf.write("\u016d\7p\2\2\u016b\u016d\7\2\2\3\u016c\u0169\3\2\2\2")
        buf.write("\u016c\u016b\3\2\2\2\u016d\u0171\3\2\2\2\u016e\u0170\13")
        buf.write("\2\2\2\u016f\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0174\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0174\u0194\7$\2\2\u0175\u0179\7$\2\2\u0176")
        buf.write("\u0178\13\2\2\2\u0177\u0176\3\2\2\2\u0178\u017b\3\2\2")
        buf.write("\2\u0179\u017a\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017f")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017d\7^\2\2\u017d")
        buf.write("\u0180\7p\2\2\u017e\u0180\7\2\2\3\u017f\u017c\3\2\2\2")
        buf.write("\u017f\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0194\7")
        buf.write("$\2\2\u0182\u0186\7$\2\2\u0183\u0184\7^\2\2\u0184\u0187")
        buf.write("\7p\2\2\u0185\u0187\7\2\2\3\u0186\u0183\3\2\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0187\u018b\3\2\2\2\u0188\u018a\13\2\2")
        buf.write("\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u0191\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018e\u018f\7^\2\2\u018f\u0192\7p\2\2\u0190")
        buf.write("\u0192\7\2\2\3\u0191\u018e\3\2\2\2\u0191\u0190\3\2\2\2")
        buf.write("\u0192\u0194\3\2\2\2\u0193\u0168\3\2\2\2\u0193\u0175\3")
        buf.write("\2\2\2\u0193\u0182\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196")
        buf.write("\b\65\3\2\u0196j\3\2\2\2\u0197\u019b\t\3\2\2\u0198\u019a")
        buf.write("\t\4\2\2\u0199\u0198\3\2\2\2\u019a\u019d\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019cl\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019e\u019f\5q9\2\u019f\u01a0\b\67\4\2")
        buf.write("\u01a0n\3\2\2\2\u01a1\u01a3\5q9\2\u01a2\u01a4\5s:\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a6\3\2\2\2")
        buf.write("\u01a5\u01a7\5u;\2\u01a6\u01a5\3\2\2\2\u01a6\u01a7\3\2")
        buf.write("\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\b8\5\2\u01a9p\3\2")
        buf.write("\2\2\u01aa\u01bd\7\62\2\2\u01ab\u01ad\t\5\2\2\u01ac\u01ab")
        buf.write("\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01b9\t\6\2\2\u01af\u01b1\7a\2\2\u01b0\u01af\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01b4\t")
        buf.write("\7\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7")
        buf.write("\u01b0\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01b9\u01ba\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3")
        buf.write("\2\2\2\u01bc\u01aa\3\2\2\2\u01bc\u01ac\3\2\2\2\u01bdr")
        buf.write("\3\2\2\2\u01be\u01c0\7\60\2\2\u01bf\u01c1\t\7\2\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c0\3\2\2\2")
        buf.write("\u01c2\u01c3\3\2\2\2\u01c3t\3\2\2\2\u01c4\u01c6\t\b\2")
        buf.write("\2\u01c5\u01c7\t\5\2\2\u01c6\u01c5\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01ca\t\7\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01ccv\3\2\2\2\u01cd\u01de\7$\2\2")
        buf.write("\u01ce\u01dd\n\t\2\2\u01cf\u01d0\7^\2\2\u01d0\u01dd\7")
        buf.write("v\2\2\u01d1\u01d2\7^\2\2\u01d2\u01dd\7t\2\2\u01d3\u01d4")
        buf.write("\7^\2\2\u01d4\u01dd\7p\2\2\u01d5\u01d6\7^\2\2\u01d6\u01dd")
        buf.write("\7d\2\2\u01d7\u01d8\7^\2\2\u01d8\u01dd\7h\2\2\u01d9\u01dd")
        buf.write("\5y=\2\u01da\u01dd\5{>\2\u01db\u01dd\5}?\2\u01dc\u01ce")
        buf.write("\3\2\2\2\u01dc\u01cf\3\2\2\2\u01dc\u01d1\3\2\2\2\u01dc")
        buf.write("\u01d3\3\2\2\2\u01dc\u01d5\3\2\2\2\u01dc\u01d7\3\2\2\2")
        buf.write("\u01dc\u01d9\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db\3")
        buf.write("\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df")
        buf.write("\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1")
        buf.write("\u01e2\7$\2\2\u01e2\u01e3\b<\6\2\u01e3x\3\2\2\2\u01e4")
        buf.write("\u01e5\7^\2\2\u01e5\u01e6\7)\2\2\u01e6z\3\2\2\2\u01e7")
        buf.write("\u01e8\7^\2\2\u01e8\u01e9\7$\2\2\u01e9|\3\2\2\2\u01ea")
        buf.write("\u01eb\7^\2\2\u01eb\u01ec\7^\2\2\u01ec~\3\2\2\2\u01ed")
        buf.write("\u01ef\t\n\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\3")
        buf.write("\2\2\2\u01f2\u01f3\b@\2\2\u01f3\u0080\3\2\2\2\u01f4\u01f5")
        buf.write("\13\2\2\2\u01f5\u01f6\bA\7\2\u01f6\u0082\3\2\2\2\u01f7")
        buf.write("\u01fb\7$\2\2\u01f8\u01fa\n\13\2\2\u01f9\u01f8\3\2\2\2")
        buf.write("\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3")
        buf.write("\2\2\2\u01fc\u01fe\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u01ff")
        buf.write("\bB\b\2\u01ff\u0084\3\2\2\2\34\2\u0155\u0163\u016c\u0171")
        buf.write("\u0179\u017f\u0186\u018b\u0191\u0193\u019b\u01a3\u01a6")
        buf.write("\u01ac\u01b0\u01b5\u01b9\u01bc\u01c2\u01c6\u01cb\u01dc")
        buf.write("\u01de\u01f0\u01fb\t\b\2\2\3\65\2\3\67\3\38\4\3<\5\3A")
        buf.write("\6\3B\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    AUTO = 3
    BREAK = 4
    BOOLEAN = 5
    DO = 6
    ELSE = 7
    FALSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    TRUE = 16
    WHILE = 17
    VOID = 18
    OUT = 19
    CONTINUE = 20
    OF = 21
    INHERIT = 22
    ARRAY = 23
    ADDOP = 24
    SUBOP = 25
    MULOP = 26
    DIVOP = 27
    MODULO = 28
    LOGICNOT = 29
    AND = 30
    OR = 31
    EQ = 32
    NOTEQ = 33
    LESS = 34
    LESSOREQ = 35
    MORE_ = 36
    MOREOREQ = 37
    DBLCOL = 38
    LP = 39
    RP = 40
    LSB = 41
    RSB = 42
    DOT = 43
    COMMA = 44
    SEMI = 45
    COLON = 46
    LCB = 47
    RCB = 48
    ASSIGN = 49
    COMMENT = 50
    LINE_COMMENT = 51
    ILLEGAL_ESCAPE = 52
    ID = 53
    INT_TYPE = 54
    FLOAT_TYPE = 55
    STRING_TYPE = 56
    WS = 57
    ERROR_CHAR = 58
    UNCLOSE_STRING = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'for_stmt'", "'while_stmt'", "'auto'", "'break'", "'boolean'", 
            "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
            "'if'", "'integer'", "'return'", "'string'", "'true'", "'while'", 
            "'void'", "'out'", "'continue'", "'of'", "'inherit'", "'array'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODULO", "LOGICNOT", "AND", 
            "OR", "EQ", "NOTEQ", "LESS", "LESSOREQ", "MORE_", "MOREOREQ", 
            "DBLCOL", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", 
            "COLON", "LCB", "RCB", "ASSIGN", "COMMENT", "LINE_COMMENT", 
            "ILLEGAL_ESCAPE", "ID", "INT_TYPE", "FLOAT_TYPE", "STRING_TYPE", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                  "MODULO", "LOGICNOT", "AND", "OR", "EQ", "NOTEQ", "LESS", 
                  "LESSOREQ", "MORE_", "MOREOREQ", "DBLCOL", "LP", "RP", 
                  "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "LCB", 
                  "RCB", "ASSIGN", "COMMENT", "LINE_COMMENT", "ILLEGAL_ESCAPE", 
                  "ID", "INT_TYPE", "FLOAT_TYPE", "INTPART", "DECIMAL", 
                  "EXPONENT", "STRING_TYPE", "QUOTE", "DBLQUOTE", "BACKSLASH", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING" ]

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
            actions[51] = self.ILLEGAL_ESCAPE_action 
            actions[53] = self.INT_TYPE_action 
            actions[54] = self.FLOAT_TYPE_action 
            actions[58] = self.STRING_TYPE_action 
            actions[63] = self.ERROR_CHAR_action 
            actions[64] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise IllegalEscape(self.text)
     

    def INT_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def FLOAT_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

    def STRING_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text=self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise UncloseString(self.text)
     


