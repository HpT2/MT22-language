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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01e8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
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
        buf.write("\3\61\3\61\3\61\7\61\u013c\n\61\f\61\16\61\u013f\13\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u014a")
        buf.write("\n\62\f\62\16\62\u014d\13\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u0155\n\63\3\63\7\63\u0158\n\63\f\63\16\63")
        buf.write("\u015b\13\63\3\63\3\63\3\63\7\63\u0160\n\63\f\63\16\63")
        buf.write("\u0163\13\63\3\63\3\63\3\63\5\63\u0168\n\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\5\63\u016f\n\63\3\63\7\63\u0172\n\63\f")
        buf.write("\63\16\63\u0175\13\63\3\63\3\63\3\63\5\63\u017a\n\63\5")
        buf.write("\63\u017c\n\63\3\63\3\63\3\64\3\64\7\64\u0182\n\64\f\64")
        buf.write("\16\64\u0185\13\64\3\65\3\65\3\65\3\66\3\66\5\66\u018c")
        buf.write("\n\66\3\66\5\66\u018f\n\66\3\66\3\66\3\67\3\67\5\67\u0195")
        buf.write("\n\67\3\67\3\67\5\67\u0199\n\67\3\67\6\67\u019c\n\67\r")
        buf.write("\67\16\67\u019d\7\67\u01a0\n\67\f\67\16\67\u01a3\13\67")
        buf.write("\5\67\u01a5\n\67\38\38\68\u01a9\n8\r8\168\u01aa\39\39")
        buf.write("\59\u01af\n9\39\69\u01b2\n9\r9\169\u01b3\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\7:\u01c5\n:\f:\16:\u01c8")
        buf.write("\13:\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>\6>\u01d7\n")
        buf.write(">\r>\16>\u01d8\3>\3>\3?\3?\3?\3@\3@\7@\u01e2\n@\f@\16")
        buf.write("@\u01e5\13@\3@\3@\6\u013d\u0159\u0161\u0173\2A\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s8u\2w\2")
        buf.write("y\2{9}:\177;\3\2\r\4\2\f\f\17\17\3\3\f\f\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\4\2--//\3\2\63;\3\2\62;\4\2GGgg\5\2$$))")
        buf.write("^^\5\2\13\f\17\17\"\"\3\2$$\2\u0202\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2s\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\3\u0081\3\2\2\2\5\u0086\3\2\2\2\7\u008c\3\2\2\2\t")
        buf.write("\u0094\3\2\2\2\13\u0097\3\2\2\2\r\u009c\3\2\2\2\17\u00a2")
        buf.write("\3\2\2\2\21\u00a8\3\2\2\2\23\u00ac\3\2\2\2\25\u00b5\3")
        buf.write("\2\2\2\27\u00b8\3\2\2\2\31\u00c0\3\2\2\2\33\u00c7\3\2")
        buf.write("\2\2\35\u00ce\3\2\2\2\37\u00d3\3\2\2\2!\u00d9\3\2\2\2")
        buf.write("#\u00de\3\2\2\2%\u00e2\3\2\2\2\'\u00eb\3\2\2\2)\u00ee")
        buf.write("\3\2\2\2+\u00f6\3\2\2\2-\u00fc\3\2\2\2/\u00fe\3\2\2\2")
        buf.write("\61\u0100\3\2\2\2\63\u0102\3\2\2\2\65\u0104\3\2\2\2\67")
        buf.write("\u0106\3\2\2\29\u0108\3\2\2\2;\u010b\3\2\2\2=\u010e\3")
        buf.write("\2\2\2?\u0111\3\2\2\2A\u0114\3\2\2\2C\u0116\3\2\2\2E\u0119")
        buf.write("\3\2\2\2G\u011b\3\2\2\2I\u011e\3\2\2\2K\u0121\3\2\2\2")
        buf.write("M\u0123\3\2\2\2O\u0125\3\2\2\2Q\u0127\3\2\2\2S\u0129\3")
        buf.write("\2\2\2U\u012b\3\2\2\2W\u012d\3\2\2\2Y\u012f\3\2\2\2[\u0131")
        buf.write("\3\2\2\2]\u0133\3\2\2\2_\u0135\3\2\2\2a\u0137\3\2\2\2")
        buf.write("c\u0145\3\2\2\2e\u017b\3\2\2\2g\u017f\3\2\2\2i\u0186\3")
        buf.write("\2\2\2k\u0189\3\2\2\2m\u01a4\3\2\2\2o\u01a6\3\2\2\2q\u01ac")
        buf.write("\3\2\2\2s\u01b5\3\2\2\2u\u01cc\3\2\2\2w\u01cf\3\2\2\2")
        buf.write("y\u01d2\3\2\2\2{\u01d6\3\2\2\2}\u01dc\3\2\2\2\177\u01df")
        buf.write("\3\2\2\2\u0081\u0082\7c\2\2\u0082\u0083\7w\2\2\u0083\u0084")
        buf.write("\7v\2\2\u0084\u0085\7q\2\2\u0085\4\3\2\2\2\u0086\u0087")
        buf.write("\7d\2\2\u0087\u0088\7t\2\2\u0088\u0089\7g\2\2\u0089\u008a")
        buf.write("\7c\2\2\u008a\u008b\7m\2\2\u008b\6\3\2\2\2\u008c\u008d")
        buf.write("\7d\2\2\u008d\u008e\7q\2\2\u008e\u008f\7q\2\2\u008f\u0090")
        buf.write("\7n\2\2\u0090\u0091\7g\2\2\u0091\u0092\7c\2\2\u0092\u0093")
        buf.write("\7p\2\2\u0093\b\3\2\2\2\u0094\u0095\7f\2\2\u0095\u0096")
        buf.write("\7q\2\2\u0096\n\3\2\2\2\u0097\u0098\7g\2\2\u0098\u0099")
        buf.write("\7n\2\2\u0099\u009a\7u\2\2\u009a\u009b\7g\2\2\u009b\f")
        buf.write("\3\2\2\2\u009c\u009d\7h\2\2\u009d\u009e\7c\2\2\u009e\u009f")
        buf.write("\7n\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\16")
        buf.write("\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5")
        buf.write("\7q\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7v\2\2\u00a7\20")
        buf.write("\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\22\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae")
        buf.write("\7w\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7e\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4")
        buf.write("\7p\2\2\u00b4\24\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7")
        buf.write("\7h\2\2\u00b7\26\3\2\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba")
        buf.write("\7p\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd")
        buf.write("\7i\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7t\2\2\u00bf\30")
        buf.write("\3\2\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7v\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6")
        buf.write("\7p\2\2\u00c6\32\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7i\2\2\u00cd\34\3\2\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2")
        buf.write("\7g\2\2\u00d2\36\3\2\2\2\u00d3\u00d4\7y\2\2\u00d4\u00d5")
        buf.write("\7j\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8 \3\2\2\2\u00d9\u00da\7x\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7f\2\2\u00dd\"")
        buf.write("\3\2\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1$\3\2\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea&\3\2\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7h\2\2\u00ed(\3\2\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7j\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7v\2\2\u00f5*\3")
        buf.write("\2\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7{\2\2\u00fb,\3")
        buf.write("\2\2\2\u00fc\u00fd\7-\2\2\u00fd.\3\2\2\2\u00fe\u00ff\7")
        buf.write("/\2\2\u00ff\60\3\2\2\2\u0100\u0101\7,\2\2\u0101\62\3\2")
        buf.write("\2\2\u0102\u0103\7\61\2\2\u0103\64\3\2\2\2\u0104\u0105")
        buf.write("\7\'\2\2\u0105\66\3\2\2\2\u0106\u0107\7#\2\2\u01078\3")
        buf.write("\2\2\2\u0108\u0109\7(\2\2\u0109\u010a\7(\2\2\u010a:\3")
        buf.write("\2\2\2\u010b\u010c\7~\2\2\u010c\u010d\7~\2\2\u010d<\3")
        buf.write("\2\2\2\u010e\u010f\7?\2\2\u010f\u0110\7?\2\2\u0110>\3")
        buf.write("\2\2\2\u0111\u0112\7#\2\2\u0112\u0113\7?\2\2\u0113@\3")
        buf.write("\2\2\2\u0114\u0115\7>\2\2\u0115B\3\2\2\2\u0116\u0117\7")
        buf.write(">\2\2\u0117\u0118\7?\2\2\u0118D\3\2\2\2\u0119\u011a\7")
        buf.write("@\2\2\u011aF\3\2\2\2\u011b\u011c\7@\2\2\u011c\u011d\7")
        buf.write("?\2\2\u011dH\3\2\2\2\u011e\u011f\7<\2\2\u011f\u0120\7")
        buf.write("<\2\2\u0120J\3\2\2\2\u0121\u0122\7*\2\2\u0122L\3\2\2\2")
        buf.write("\u0123\u0124\7+\2\2\u0124N\3\2\2\2\u0125\u0126\7]\2\2")
        buf.write("\u0126P\3\2\2\2\u0127\u0128\7_\2\2\u0128R\3\2\2\2\u0129")
        buf.write("\u012a\7\60\2\2\u012aT\3\2\2\2\u012b\u012c\7.\2\2\u012c")
        buf.write("V\3\2\2\2\u012d\u012e\7=\2\2\u012eX\3\2\2\2\u012f\u0130")
        buf.write("\7<\2\2\u0130Z\3\2\2\2\u0131\u0132\7}\2\2\u0132\\\3\2")
        buf.write("\2\2\u0133\u0134\7\177\2\2\u0134^\3\2\2\2\u0135\u0136")
        buf.write("\7?\2\2\u0136`\3\2\2\2\u0137\u0138\7\61\2\2\u0138\u0139")
        buf.write("\7,\2\2\u0139\u013d\3\2\2\2\u013a\u013c\13\2\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013d\u013b\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u013d\3")
        buf.write("\2\2\2\u0140\u0141\7,\2\2\u0141\u0142\7\61\2\2\u0142\u0143")
        buf.write("\3\2\2\2\u0143\u0144\b\61\2\2\u0144b\3\2\2\2\u0145\u0146")
        buf.write("\7\61\2\2\u0146\u0147\7\61\2\2\u0147\u014b\3\2\2\2\u0148")
        buf.write("\u014a\n\2\2\2\u0149\u0148\3\2\2\2\u014a\u014d\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e\3")
        buf.write("\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\b\62\2\2\u014f")
        buf.write("d\3\2\2\2\u0150\u0154\7$\2\2\u0151\u0152\7^\2\2\u0152")
        buf.write("\u0155\7p\2\2\u0153\u0155\t\3\2\2\u0154\u0151\3\2\2\2")
        buf.write("\u0154\u0153\3\2\2\2\u0155\u0159\3\2\2\2\u0156\u0158\13")
        buf.write("\2\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u015a")
        buf.write("\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015c\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015c\u017c\7$\2\2\u015d\u0161\7$\2\2\u015e")
        buf.write("\u0160\13\2\2\2\u015f\u015e\3\2\2\2\u0160\u0163\3\2\2")
        buf.write("\2\u0161\u0162\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0167")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\7^\2\2\u0165")
        buf.write("\u0168\7p\2\2\u0166\u0168\7\2\2\3\u0167\u0164\3\2\2\2")
        buf.write("\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u017c\7")
        buf.write("$\2\2\u016a\u016e\7$\2\2\u016b\u016c\7^\2\2\u016c\u016f")
        buf.write("\7p\2\2\u016d\u016f\7\2\2\3\u016e\u016b\3\2\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016f\u0173\3\2\2\2\u0170\u0172\13\2\2")
        buf.write("\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0179\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0176\u0177\7^\2\2\u0177\u017a\7p\2\2\u0178")
        buf.write("\u017a\7\2\2\3\u0179\u0176\3\2\2\2\u0179\u0178\3\2\2\2")
        buf.write("\u017a\u017c\3\2\2\2\u017b\u0150\3\2\2\2\u017b\u015d\3")
        buf.write("\2\2\2\u017b\u016a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e")
        buf.write("\b\63\3\2\u017ef\3\2\2\2\u017f\u0183\t\4\2\2\u0180\u0182")
        buf.write("\t\5\2\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2\2\2\u0183")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184h\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0186\u0187\5m\67\2\u0187\u0188\b\65\4")
        buf.write("\2\u0188j\3\2\2\2\u0189\u018b\5m\67\2\u018a\u018c\5o8")
        buf.write("\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e")
        buf.write("\3\2\2\2\u018d\u018f\5q9\2\u018e\u018d\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\b\66\5\2\u0191")
        buf.write("l\3\2\2\2\u0192\u01a5\7\62\2\2\u0193\u0195\t\6\2\2\u0194")
        buf.write("\u0193\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u01a1\t\7\2\2\u0197\u0199\7a\2\2\u0198\u0197\3")
        buf.write("\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3\2\2\2\u019a\u019c")
        buf.write("\t\b\2\2\u019b\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a0\3\2\2\2")
        buf.write("\u019f\u0198\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3")
        buf.write("\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a4\u0192\3\2\2\2\u01a4\u0194\3\2\2\2\u01a5")
        buf.write("n\3\2\2\2\u01a6\u01a8\7\60\2\2\u01a7\u01a9\t\b\2\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01aa\u01ab\3\2\2\2\u01abp\3\2\2\2\u01ac\u01ae\t\t\2")
        buf.write("\2\u01ad\u01af\t\6\2\2\u01ae\u01ad\3\2\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01b2\t\b\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4r\3\2\2\2\u01b5\u01c6\7$\2\2")
        buf.write("\u01b6\u01c5\n\n\2\2\u01b7\u01b8\7^\2\2\u01b8\u01c5\7")
        buf.write("v\2\2\u01b9\u01ba\7^\2\2\u01ba\u01c5\7t\2\2\u01bb\u01bc")
        buf.write("\7^\2\2\u01bc\u01c5\7p\2\2\u01bd\u01be\7^\2\2\u01be\u01c5")
        buf.write("\7d\2\2\u01bf\u01c0\7^\2\2\u01c0\u01c5\7h\2\2\u01c1\u01c5")
        buf.write("\5u;\2\u01c2\u01c5\5w<\2\u01c3\u01c5\5y=\2\u01c4\u01b6")
        buf.write("\3\2\2\2\u01c4\u01b7\3\2\2\2\u01c4\u01b9\3\2\2\2\u01c4")
        buf.write("\u01bb\3\2\2\2\u01c4\u01bd\3\2\2\2\u01c4\u01bf\3\2\2\2")
        buf.write("\u01c4\u01c1\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3")
        buf.write("\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9")
        buf.write("\u01ca\7$\2\2\u01ca\u01cb\b:\6\2\u01cbt\3\2\2\2\u01cc")
        buf.write("\u01cd\7^\2\2\u01cd\u01ce\7)\2\2\u01cev\3\2\2\2\u01cf")
        buf.write("\u01d0\7^\2\2\u01d0\u01d1\7$\2\2\u01d1x\3\2\2\2\u01d2")
        buf.write("\u01d3\7^\2\2\u01d3\u01d4\7^\2\2\u01d4z\3\2\2\2\u01d5")
        buf.write("\u01d7\t\13\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8\3\2\2")
        buf.write("\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01da\u01db\b>\2\2\u01db|\3\2\2\2\u01dc\u01dd")
        buf.write("\13\2\2\2\u01dd\u01de\b?\7\2\u01de~\3\2\2\2\u01df\u01e3")
        buf.write("\7$\2\2\u01e0\u01e2\n\f\2\2\u01e1\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4\u01e6\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7\b")
        buf.write("@\b\2\u01e7\u0080\3\2\2\2\34\2\u013d\u014b\u0154\u0159")
        buf.write("\u0161\u0167\u016e\u0173\u0179\u017b\u0183\u018b\u018e")
        buf.write("\u0194\u0198\u019d\u01a1\u01a4\u01aa\u01ae\u01b3\u01c4")
        buf.write("\u01c6\u01d8\u01e3\t\b\2\2\3\63\2\3\65\3\3\66\4\3:\5\3")
        buf.write("?\6\3@\7")
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
    ILLEGAL_ESCAPE = 50
    ID = 51
    INT_TYPE = 52
    FLOAT_TYPE = 53
    STRING_TYPE = 54
    WS = 55
    ERROR_CHAR = 56
    UNCLOSE_STRING = 57

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
            "ILLEGAL_ESCAPE", "ID", "INT_TYPE", "FLOAT_TYPE", "STRING_TYPE", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODULO", 
                  "LOGICNOT", "AND", "OR", "EQ", "NOTEQ", "LESS", "LESSOREQ", 
                  "MORE_", "MOREOREQ", "DBLCOL", "LP", "RP", "LSB", "RSB", 
                  "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "ASSIGN", 
                  "COMMENT", "LINE_COMMENT", "ILLEGAL_ESCAPE", "ID", "INT_TYPE", 
                  "FLOAT_TYPE", "INTPART", "DECIMAL", "EXPONENT", "STRING_TYPE", 
                  "QUOTE", "DBLQUOTE", "BACKSLASH", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING" ]

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
            actions[49] = self.ILLEGAL_ESCAPE_action 
            actions[51] = self.INT_TYPE_action 
            actions[52] = self.FLOAT_TYPE_action 
            actions[56] = self.STRING_TYPE_action 
            actions[61] = self.ERROR_CHAR_action 
            actions[62] = self.UNCLOSE_STRING_action 
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
     


