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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u024c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3")
        buf.write(":\3:\7:\u01bb\n:\f:\16:\u01be\13:\3:\3:\3:\3:\3:\3;\3")
        buf.write(";\3;\3;\7;\u01c9\n;\f;\16;\u01cc\13;\3;\3;\3<\3<\7<\u01d2")
        buf.write("\n<\f<\16<\u01d5\13<\3=\3=\3=\3>\3>\5>\u01dc\n>\3>\5>")
        buf.write("\u01df\n>\3>\3>\3?\3?\3?\5?\u01e6\n?\3?\6?\u01e9\n?\r")
        buf.write("?\16?\u01ea\7?\u01ed\n?\f?\16?\u01f0\13?\5?\u01f2\n?\3")
        buf.write("@\3@\6@\u01f6\n@\r@\16@\u01f7\3A\3A\5A\u01fc\nA\3A\6A")
        buf.write("\u01ff\nA\rA\16A\u0200\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\7B\u0214\nB\fB\16B\u0217\13B\3B\3")
        buf.write("B\3B\5B\u021c\nB\3C\3C\3C\3D\3D\3D\3E\3E\3E\3F\6F\u0228")
        buf.write("\nF\rF\16F\u0229\3F\3F\3G\3G\3G\3H\3H\7H\u0233\nH\fH\16")
        buf.write("H\u0236\13H\3H\3H\3I\3I\7I\u023c\nI\fI\16I\u023f\13I\3")
        buf.write("I\5I\u0242\nI\3I\7I\u0245\nI\fI\16I\u0248\13I\3I\3I\3")
        buf.write("I\5\u01bc\u023d\u0246\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}\2\177\2\u0081\2\u0083")
        buf.write("@\u0085\2\u0087\2\u0089\2\u008bA\u008dB\u008fC\u0091D")
        buf.write("\3\2\16\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63")
        buf.write(";\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$))\3\2\f\f\5\2\13\f")
        buf.write("\17\17\"\"\4\2\f\f$$\3\3\f\f\2\u025f\2\3\3\2\2\2\2\5\3")
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
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u009f\3\2\2\2\7\u00ac")
        buf.write("\3\2\2\2\t\u00b6\3\2\2\2\13\u00c1\3\2\2\2\r\u00cd\3\2")
        buf.write("\2\2\17\u00da\3\2\2\2\21\u00e5\3\2\2\2\23\u00f1\3\2\2")
        buf.write("\2\25\u0100\3\2\2\2\27\u0105\3\2\2\2\31\u010b\3\2\2\2")
        buf.write("\33\u0113\3\2\2\2\35\u0116\3\2\2\2\37\u011b\3\2\2\2!\u0121")
        buf.write("\3\2\2\2#\u0127\3\2\2\2%\u012b\3\2\2\2\'\u0134\3\2\2\2")
        buf.write(")\u0137\3\2\2\2+\u013f\3\2\2\2-\u0146\3\2\2\2/\u014d\3")
        buf.write("\2\2\2\61\u0152\3\2\2\2\63\u0158\3\2\2\2\65\u015d\3\2")
        buf.write("\2\2\67\u0161\3\2\2\29\u016a\3\2\2\2;\u016d\3\2\2\2=\u0175")
        buf.write("\3\2\2\2?\u017b\3\2\2\2A\u017d\3\2\2\2C\u017f\3\2\2\2")
        buf.write("E\u0181\3\2\2\2G\u0183\3\2\2\2I\u0185\3\2\2\2K\u0187\3")
        buf.write("\2\2\2M\u018a\3\2\2\2O\u018d\3\2\2\2Q\u0190\3\2\2\2S\u0193")
        buf.write("\3\2\2\2U\u0195\3\2\2\2W\u0198\3\2\2\2Y\u019a\3\2\2\2")
        buf.write("[\u019d\3\2\2\2]\u01a0\3\2\2\2_\u01a2\3\2\2\2a\u01a4\3")
        buf.write("\2\2\2c\u01a6\3\2\2\2e\u01a8\3\2\2\2g\u01aa\3\2\2\2i\u01ac")
        buf.write("\3\2\2\2k\u01ae\3\2\2\2m\u01b0\3\2\2\2o\u01b2\3\2\2\2")
        buf.write("q\u01b4\3\2\2\2s\u01b6\3\2\2\2u\u01c4\3\2\2\2w\u01cf\3")
        buf.write("\2\2\2y\u01d6\3\2\2\2{\u01d9\3\2\2\2}\u01f1\3\2\2\2\177")
        buf.write("\u01f3\3\2\2\2\u0081\u01f9\3\2\2\2\u0083\u021b\3\2\2\2")
        buf.write("\u0085\u021d\3\2\2\2\u0087\u0220\3\2\2\2\u0089\u0223\3")
        buf.write("\2\2\2\u008b\u0227\3\2\2\2\u008d\u022d\3\2\2\2\u008f\u0230")
        buf.write("\3\2\2\2\u0091\u0239\3\2\2\2\u0093\u0094\7t\2\2\u0094")
        buf.write("\u0095\7g\2\2\u0095\u0096\7c\2\2\u0096\u0097\7f\2\2\u0097")
        buf.write("\u0098\7K\2\2\u0098\u0099\7p\2\2\u0099\u009a\7v\2\2\u009a")
        buf.write("\u009b\7g\2\2\u009b\u009c\7i\2\2\u009c\u009d\7g\2\2\u009d")
        buf.write("\u009e\7t\2\2\u009e\4\3\2\2\2\u009f\u00a0\7r\2\2\u00a0")
        buf.write("\u00a1\7t\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7p\2\2\u00a3")
        buf.write("\u00a4\7v\2\2\u00a4\u00a5\7K\2\2\u00a5\u00a6\7p\2\2\u00a6")
        buf.write("\u00a7\7v\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7i\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\u00ab\7t\2\2\u00ab\6\3\2\2\2\u00ac")
        buf.write("\u00ad\7t\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7c\2\2\u00af")
        buf.write("\u00b0\7f\2\2\u00b0\u00b1\7H\2\2\u00b1\u00b2\7n\2\2\u00b2")
        buf.write("\u00b3\7q\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7v\2\2\u00b5")
        buf.write("\b\3\2\2\2\u00b6\u00b7\7y\2\2\u00b7\u00b8\7t\2\2\u00b8")
        buf.write("\u00b9\7k\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7g\2\2\u00bb")
        buf.write("\u00bc\7H\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7q\2\2\u00be")
        buf.write("\u00bf\7c\2\2\u00bf\u00c0\7v\2\2\u00c0\n\3\2\2\2\u00c1")
        buf.write("\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7c\2\2\u00c4")
        buf.write("\u00c5\7f\2\2\u00c5\u00c6\7D\2\2\u00c6\u00c7\7q\2\2\u00c7")
        buf.write("\u00c8\7q\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\u00cb\7c\2\2\u00cb\u00cc\7p\2\2\u00cc\f\3\2\2\2\u00cd")
        buf.write("\u00ce\7r\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0\7k\2\2\u00d0")
        buf.write("\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7D\2\2\u00d3")
        buf.write("\u00d4\7q\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7n\2\2\u00d6")
        buf.write("\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7p\2\2\u00d9")
        buf.write("\16\3\2\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7g\2\2\u00dc")
        buf.write("\u00dd\7c\2\2\u00dd\u00de\7f\2\2\u00de\u00df\7U\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2")
        buf.write("\u00e3\7p\2\2\u00e3\u00e4\7i\2\2\u00e4\20\3\2\2\2\u00e5")
        buf.write("\u00e6\7r\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7k\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7U\2\2\u00eb")
        buf.write("\u00ec\7v\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7k\2\2\u00ee")
        buf.write("\u00ef\7p\2\2\u00ef\u00f0\7i\2\2\u00f0\22\3\2\2\2\u00f1")
        buf.write("\u00f2\7r\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7g\2\2\u00f4")
        buf.write("\u00f5\7x\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\u00f8\7v\2\2\u00f8\u00f9\7F\2\2\u00f9\u00fa\7g\2\2\u00fa")
        buf.write("\u00fb\7h\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7w\2\2\u00fd")
        buf.write("\u00fe\7n\2\2\u00fe\u00ff\7v\2\2\u00ff\24\3\2\2\2\u0100")
        buf.write("\u0101\7c\2\2\u0101\u0102\7w\2\2\u0102\u0103\7v\2\2\u0103")
        buf.write("\u0104\7q\2\2\u0104\26\3\2\2\2\u0105\u0106\7d\2\2\u0106")
        buf.write("\u0107\7t\2\2\u0107\u0108\7g\2\2\u0108\u0109\7c\2\2\u0109")
        buf.write("\u010a\7m\2\2\u010a\30\3\2\2\2\u010b\u010c\7d\2\2\u010c")
        buf.write("\u010d\7q\2\2\u010d\u010e\7q\2\2\u010e\u010f\7n\2\2\u010f")
        buf.write("\u0110\7g\2\2\u0110\u0111\7c\2\2\u0111\u0112\7p\2\2\u0112")
        buf.write("\32\3\2\2\2\u0113\u0114\7f\2\2\u0114\u0115\7q\2\2\u0115")
        buf.write("\34\3\2\2\2\u0116\u0117\7g\2\2\u0117\u0118\7n\2\2\u0118")
        buf.write("\u0119\7u\2\2\u0119\u011a\7g\2\2\u011a\36\3\2\2\2\u011b")
        buf.write("\u011c\7h\2\2\u011c\u011d\7c\2\2\u011d\u011e\7n\2\2\u011e")
        buf.write("\u011f\7u\2\2\u011f\u0120\7g\2\2\u0120 \3\2\2\2\u0121")
        buf.write("\u0122\7h\2\2\u0122\u0123\7n\2\2\u0123\u0124\7q\2\2\u0124")
        buf.write("\u0125\7c\2\2\u0125\u0126\7v\2\2\u0126\"\3\2\2\2\u0127")
        buf.write("\u0128\7h\2\2\u0128\u0129\7q\2\2\u0129\u012a\7t\2\2\u012a")
        buf.write("$\3\2\2\2\u012b\u012c\7h\2\2\u012c\u012d\7w\2\2\u012d")
        buf.write("\u012e\7p\2\2\u012e\u012f\7e\2\2\u012f\u0130\7v\2\2\u0130")
        buf.write("\u0131\7k\2\2\u0131\u0132\7q\2\2\u0132\u0133\7p\2\2\u0133")
        buf.write("&\3\2\2\2\u0134\u0135\7k\2\2\u0135\u0136\7h\2\2\u0136")
        buf.write("(\3\2\2\2\u0137\u0138\7k\2\2\u0138\u0139\7p\2\2\u0139")
        buf.write("\u013a\7v\2\2\u013a\u013b\7g\2\2\u013b\u013c\7i\2\2\u013c")
        buf.write("\u013d\7g\2\2\u013d\u013e\7t\2\2\u013e*\3\2\2\2\u013f")
        buf.write("\u0140\7t\2\2\u0140\u0141\7g\2\2\u0141\u0142\7v\2\2\u0142")
        buf.write("\u0143\7w\2\2\u0143\u0144\7t\2\2\u0144\u0145\7p\2\2\u0145")
        buf.write(",\3\2\2\2\u0146\u0147\7u\2\2\u0147\u0148\7v\2\2\u0148")
        buf.write("\u0149\7t\2\2\u0149\u014a\7k\2\2\u014a\u014b\7p\2\2\u014b")
        buf.write("\u014c\7i\2\2\u014c.\3\2\2\2\u014d\u014e\7v\2\2\u014e")
        buf.write("\u014f\7t\2\2\u014f\u0150\7w\2\2\u0150\u0151\7g\2\2\u0151")
        buf.write("\60\3\2\2\2\u0152\u0153\7y\2\2\u0153\u0154\7j\2\2\u0154")
        buf.write("\u0155\7k\2\2\u0155\u0156\7n\2\2\u0156\u0157\7g\2\2\u0157")
        buf.write("\62\3\2\2\2\u0158\u0159\7x\2\2\u0159\u015a\7q\2\2\u015a")
        buf.write("\u015b\7k\2\2\u015b\u015c\7f\2\2\u015c\64\3\2\2\2\u015d")
        buf.write("\u015e\7q\2\2\u015e\u015f\7w\2\2\u015f\u0160\7v\2\2\u0160")
        buf.write("\66\3\2\2\2\u0161\u0162\7e\2\2\u0162\u0163\7q\2\2\u0163")
        buf.write("\u0164\7p\2\2\u0164\u0165\7v\2\2\u0165\u0166\7k\2\2\u0166")
        buf.write("\u0167\7p\2\2\u0167\u0168\7w\2\2\u0168\u0169\7g\2\2\u0169")
        buf.write("8\3\2\2\2\u016a\u016b\7q\2\2\u016b\u016c\7h\2\2\u016c")
        buf.write(":\3\2\2\2\u016d\u016e\7k\2\2\u016e\u016f\7p\2\2\u016f")
        buf.write("\u0170\7j\2\2\u0170\u0171\7g\2\2\u0171\u0172\7t\2\2\u0172")
        buf.write("\u0173\7k\2\2\u0173\u0174\7v\2\2\u0174<\3\2\2\2\u0175")
        buf.write("\u0176\7c\2\2\u0176\u0177\7t\2\2\u0177\u0178\7t\2\2\u0178")
        buf.write("\u0179\7c\2\2\u0179\u017a\7{\2\2\u017a>\3\2\2\2\u017b")
        buf.write("\u017c\7-\2\2\u017c@\3\2\2\2\u017d\u017e\7/\2\2\u017e")
        buf.write("B\3\2\2\2\u017f\u0180\7,\2\2\u0180D\3\2\2\2\u0181\u0182")
        buf.write("\7\61\2\2\u0182F\3\2\2\2\u0183\u0184\7\'\2\2\u0184H\3")
        buf.write("\2\2\2\u0185\u0186\7#\2\2\u0186J\3\2\2\2\u0187\u0188\7")
        buf.write("(\2\2\u0188\u0189\7(\2\2\u0189L\3\2\2\2\u018a\u018b\7")
        buf.write("~\2\2\u018b\u018c\7~\2\2\u018cN\3\2\2\2\u018d\u018e\7")
        buf.write("?\2\2\u018e\u018f\7?\2\2\u018fP\3\2\2\2\u0190\u0191\7")
        buf.write("#\2\2\u0191\u0192\7?\2\2\u0192R\3\2\2\2\u0193\u0194\7")
        buf.write(">\2\2\u0194T\3\2\2\2\u0195\u0196\7>\2\2\u0196\u0197\7")
        buf.write("?\2\2\u0197V\3\2\2\2\u0198\u0199\7@\2\2\u0199X\3\2\2\2")
        buf.write("\u019a\u019b\7@\2\2\u019b\u019c\7?\2\2\u019cZ\3\2\2\2")
        buf.write("\u019d\u019e\7<\2\2\u019e\u019f\7<\2\2\u019f\\\3\2\2\2")
        buf.write("\u01a0\u01a1\7*\2\2\u01a1^\3\2\2\2\u01a2\u01a3\7+\2\2")
        buf.write("\u01a3`\3\2\2\2\u01a4\u01a5\7]\2\2\u01a5b\3\2\2\2\u01a6")
        buf.write("\u01a7\7_\2\2\u01a7d\3\2\2\2\u01a8\u01a9\7\60\2\2\u01a9")
        buf.write("f\3\2\2\2\u01aa\u01ab\7.\2\2\u01abh\3\2\2\2\u01ac\u01ad")
        buf.write("\7=\2\2\u01adj\3\2\2\2\u01ae\u01af\7<\2\2\u01afl\3\2\2")
        buf.write("\2\u01b0\u01b1\7}\2\2\u01b1n\3\2\2\2\u01b2\u01b3\7\177")
        buf.write("\2\2\u01b3p\3\2\2\2\u01b4\u01b5\7?\2\2\u01b5r\3\2\2\2")
        buf.write("\u01b6\u01b7\7\61\2\2\u01b7\u01b8\7,\2\2\u01b8\u01bc\3")
        buf.write("\2\2\2\u01b9\u01bb\13\2\2\2\u01ba\u01b9\3\2\2\2\u01bb")
        buf.write("\u01be\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0\7")
        buf.write(",\2\2\u01c0\u01c1\7\61\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3")
        buf.write("\b:\2\2\u01c3t\3\2\2\2\u01c4\u01c5\7\61\2\2\u01c5\u01c6")
        buf.write("\7\61\2\2\u01c6\u01ca\3\2\2\2\u01c7\u01c9\n\2\2\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3")
        buf.write("\2\2\2\u01cd\u01ce\b;\2\2\u01cev\3\2\2\2\u01cf\u01d3\t")
        buf.write("\3\2\2\u01d0\u01d2\t\4\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d5")
        buf.write("\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("x\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\5}?\2\u01d7")
        buf.write("\u01d8\b=\3\2\u01d8z\3\2\2\2\u01d9\u01db\5}?\2\u01da\u01dc")
        buf.write("\5\177@\2\u01db\u01da\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc")
        buf.write("\u01de\3\2\2\2\u01dd\u01df\5\u0081A\2\u01de\u01dd\3\2")
        buf.write("\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1")
        buf.write("\b>\4\2\u01e1|\3\2\2\2\u01e2\u01f2\7\62\2\2\u01e3\u01ee")
        buf.write("\t\5\2\2\u01e4\u01e6\7a\2\2\u01e5\u01e4\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e9\t\6\2\2")
        buf.write("\u01e8\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01e8\3")
        buf.write("\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed\3\2\2\2\u01ec\u01e5")
        buf.write("\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2")
        buf.write("\u01f1\u01e2\3\2\2\2\u01f1\u01e3\3\2\2\2\u01f2~\3\2\2")
        buf.write("\2\u01f3\u01f5\7\60\2\2\u01f4\u01f6\t\6\2\2\u01f5\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u0080\3\2\2\2\u01f9\u01fb\t\7\2\2")
        buf.write("\u01fa\u01fc\t\b\2\2\u01fb\u01fa\3\2\2\2\u01fb\u01fc\3")
        buf.write("\2\2\2\u01fc\u01fe\3\2\2\2\u01fd\u01ff\t\6\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u0082\3\2\2\2\u0202\u0203\7$\2\2")
        buf.write("\u0203\u021c\7$\2\2\u0204\u0215\7$\2\2\u0205\u0214\n\t")
        buf.write("\2\2\u0206\u0207\7^\2\2\u0207\u0214\7v\2\2\u0208\u0209")
        buf.write("\7^\2\2\u0209\u0214\7t\2\2\u020a\u020b\7^\2\2\u020b\u0214")
        buf.write("\7p\2\2\u020c\u020d\7^\2\2\u020d\u0214\7d\2\2\u020e\u020f")
        buf.write("\7^\2\2\u020f\u0214\7h\2\2\u0210\u0214\5\u0085C\2\u0211")
        buf.write("\u0214\5\u0087D\2\u0212\u0214\5\u0089E\2\u0213\u0205\3")
        buf.write("\2\2\2\u0213\u0206\3\2\2\2\u0213\u0208\3\2\2\2\u0213\u020a")
        buf.write("\3\2\2\2\u0213\u020c\3\2\2\2\u0213\u020e\3\2\2\2\u0213")
        buf.write("\u0210\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0212\3\2\2\2")
        buf.write("\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3")
        buf.write("\2\2\2\u0216\u0218\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u0219")
        buf.write("\n\n\2\2\u0219\u021a\7$\2\2\u021a\u021c\bB\5\2\u021b\u0202")
        buf.write("\3\2\2\2\u021b\u0204\3\2\2\2\u021c\u0084\3\2\2\2\u021d")
        buf.write("\u021e\7^\2\2\u021e\u021f\7)\2\2\u021f\u0086\3\2\2\2\u0220")
        buf.write("\u0221\7^\2\2\u0221\u0222\7$\2\2\u0222\u0088\3\2\2\2\u0223")
        buf.write("\u0224\7^\2\2\u0224\u0225\7^\2\2\u0225\u008a\3\2\2\2\u0226")
        buf.write("\u0228\t\13\2\2\u0227\u0226\3\2\2\2\u0228\u0229\3\2\2")
        buf.write("\2\u0229\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b")
        buf.write("\3\2\2\2\u022b\u022c\bF\2\2\u022c\u008c\3\2\2\2\u022d")
        buf.write("\u022e\13\2\2\2\u022e\u022f\bG\6\2\u022f\u008e\3\2\2\2")
        buf.write("\u0230\u0234\7$\2\2\u0231\u0233\n\f\2\2\u0232\u0231\3")
        buf.write("\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235")
        buf.write("\3\2\2\2\u0235\u0237\3\2\2\2\u0236\u0234\3\2\2\2\u0237")
        buf.write("\u0238\bH\7\2\u0238\u0090\3\2\2\2\u0239\u023d\7$\2\2\u023a")
        buf.write("\u023c\13\2\2\2\u023b\u023a\3\2\2\2\u023c\u023f\3\2\2")
        buf.write("\2\u023d\u023e\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u0241")
        buf.write("\3\2\2\2\u023f\u023d\3\2\2\2\u0240\u0242\t\r\2\2\u0241")
        buf.write("\u0240\3\2\2\2\u0242\u0246\3\2\2\2\u0243\u0245\13\2\2")
        buf.write("\2\u0244\u0243\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0247")
        buf.write("\3\2\2\2\u0246\u0244\3\2\2\2\u0247\u0249\3\2\2\2\u0248")
        buf.write("\u0246\3\2\2\2\u0249\u024a\7$\2\2\u024a\u024b\bI\b\2\u024b")
        buf.write("\u0092\3\2\2\2\27\2\u01bc\u01ca\u01d3\u01db\u01de\u01e5")
        buf.write("\u01ea\u01ee\u01f1\u01f7\u01fb\u0200\u0213\u0215\u021b")
        buf.write("\u0229\u0234\u023d\u0241\u0246\t\b\2\2\3=\2\3>\3\3B\4")
        buf.write("\3G\5\3H\6\3I\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    READ_INT = 1
    PRINT_INT = 2
    READ_FLOAT = 3
    WRITE_FLOAT = 4
    READ_BOOL = 5
    PRINT_BOOL = 6
    READ_STR = 7
    PRINT_STR = 8
    PREVENT_DEF = 9
    AUTO = 10
    BREAK = 11
    BOOLEAN = 12
    DO = 13
    ELSE = 14
    FALSE = 15
    FLOAT = 16
    FOR = 17
    FUNCTION = 18
    IF = 19
    INTEGER = 20
    RETURN = 21
    STRING = 22
    TRUE = 23
    WHILE = 24
    VOID = 25
    OUT = 26
    CONTINUE = 27
    OF = 28
    INHERIT = 29
    ARRAY = 30
    ADDOP = 31
    SUBOP = 32
    MULOP = 33
    DIVOP = 34
    MODULO = 35
    LOGICNOT = 36
    AND = 37
    OR = 38
    EQ = 39
    NOTEQ = 40
    LESS = 41
    LESSOREQ = 42
    MORE_ = 43
    MOREOREQ = 44
    DBLCOL = 45
    LP = 46
    RP = 47
    LSB = 48
    RSB = 49
    DOT = 50
    COMMA = 51
    SEMI = 52
    COLON = 53
    LCB = 54
    RCB = 55
    ASSIGN = 56
    COMMENT = 57
    LINE_COMMENT = 58
    ID = 59
    INT_TYPE = 60
    FLOAT_TYPE = 61
    STRING_TYPE = 62
    WS = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'preventDefault'", "'auto'", "'break'", "'boolean'", "'do'", 
            "'else'", "'false'", "'float'", "'for'", "'function'", "'if'", 
            "'integer'", "'return'", "'string'", "'true'", "'while'", "'void'", 
            "'out'", "'continue'", "'of'", "'inherit'", "'array'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", 
            "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "READ_INT", "PRINT_INT", "READ_FLOAT", "WRITE_FLOAT", "READ_BOOL", 
            "PRINT_BOOL", "READ_STR", "PRINT_STR", "PREVENT_DEF", "AUTO", 
            "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
            "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", 
            "MULOP", "DIVOP", "MODULO", "LOGICNOT", "AND", "OR", "EQ", "NOTEQ", 
            "LESS", "LESSOREQ", "MORE_", "MOREOREQ", "DBLCOL", "LP", "RP", 
            "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", 
            "ASSIGN", "COMMENT", "LINE_COMMENT", "ID", "INT_TYPE", "FLOAT_TYPE", 
            "STRING_TYPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "READ_INT", "PRINT_INT", "READ_FLOAT", "WRITE_FLOAT", 
                  "READ_BOOL", "PRINT_BOOL", "READ_STR", "PRINT_STR", "PREVENT_DEF", 
                  "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODULO", 
                  "LOGICNOT", "AND", "OR", "EQ", "NOTEQ", "LESS", "LESSOREQ", 
                  "MORE_", "MOREOREQ", "DBLCOL", "LP", "RP", "LSB", "RSB", 
                  "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "ASSIGN", 
                  "COMMENT", "LINE_COMMENT", "ID", "INT_TYPE", "FLOAT_TYPE", 
                  "INTPART", "DECIMAL", "EXPONENT", "STRING_TYPE", "QUOTE", 
                  "DBLQUOTE", "BACKSLASH", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[59] = self.INT_TYPE_action 
            actions[60] = self.FLOAT_TYPE_action 
            actions[64] = self.STRING_TYPE_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
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
     

    def STRING_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text)
     


