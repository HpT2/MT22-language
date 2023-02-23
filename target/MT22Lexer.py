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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0254\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3;\3;\7;\u01c3\n;\f;\16")
        buf.write(";\u01c6\13;\3;\3;\3;\3;\3;\3<\3<\3<\3<\7<\u01d1\n<\f<")
        buf.write("\16<\u01d4\13<\3<\3<\3=\3=\7=\u01da\n=\f=\16=\u01dd\13")
        buf.write("=\3>\3>\3>\3?\3?\5?\u01e4\n?\3?\5?\u01e7\n?\3?\3?\3@\3")
        buf.write("@\3@\5@\u01ee\n@\3@\6@\u01f1\n@\r@\16@\u01f2\7@\u01f5")
        buf.write("\n@\f@\16@\u01f8\13@\5@\u01fa\n@\3A\3A\6A\u01fe\nA\rA")
        buf.write("\16A\u01ff\3B\3B\5B\u0204\nB\3B\6B\u0207\nB\rB\16B\u0208")
        buf.write("\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\7")
        buf.write("C\u021c\nC\fC\16C\u021f\13C\3C\3C\3C\5C\u0224\nC\3D\3")
        buf.write("D\3D\3E\3E\3E\3F\3F\3F\3G\6G\u0230\nG\rG\16G\u0231\3G")
        buf.write("\3G\3H\3H\3H\3I\3I\7I\u023b\nI\fI\16I\u023e\13I\3I\3I")
        buf.write("\3J\3J\7J\u0244\nJ\fJ\16J\u0247\13J\3J\5J\u024a\nJ\3J")
        buf.write("\7J\u024d\nJ\fJ\16J\u0250\13J\3J\3J\3J\5\u01c4\u0245\u024e")
        buf.write("\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177\2\u0081\2\u0083\2\u0085A\u0087\2\u0089")
        buf.write("\2\u008b\2\u008dB\u008fC\u0091D\u0093E\3\2\16\4\2\f\f")
        buf.write("\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2G")
        buf.write("Ggg\4\2--//\5\2\f\f$$))\3\2\f\f\5\2\13\f\17\17\"\"\4\2")
        buf.write("\f\f$$\3\3\f\f\2\u0267\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0085\3")
        buf.write("\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2")
        buf.write("\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u00a1\3\2\2\2\7\u00ae")
        buf.write("\3\2\2\2\t\u00b8\3\2\2\2\13\u00c3\3\2\2\2\r\u00cf\3\2")
        buf.write("\2\2\17\u00dc\3\2\2\2\21\u00e7\3\2\2\2\23\u00f3\3\2\2")
        buf.write("\2\25\u00f9\3\2\2\2\27\u0108\3\2\2\2\31\u010d\3\2\2\2")
        buf.write("\33\u0113\3\2\2\2\35\u011b\3\2\2\2\37\u011e\3\2\2\2!\u0123")
        buf.write("\3\2\2\2#\u0129\3\2\2\2%\u012f\3\2\2\2\'\u0133\3\2\2\2")
        buf.write(")\u013c\3\2\2\2+\u013f\3\2\2\2-\u0147\3\2\2\2/\u014e\3")
        buf.write("\2\2\2\61\u0155\3\2\2\2\63\u015a\3\2\2\2\65\u0160\3\2")
        buf.write("\2\2\67\u0165\3\2\2\29\u0169\3\2\2\2;\u0172\3\2\2\2=\u0175")
        buf.write("\3\2\2\2?\u017d\3\2\2\2A\u0183\3\2\2\2C\u0185\3\2\2\2")
        buf.write("E\u0187\3\2\2\2G\u0189\3\2\2\2I\u018b\3\2\2\2K\u018d\3")
        buf.write("\2\2\2M\u018f\3\2\2\2O\u0192\3\2\2\2Q\u0195\3\2\2\2S\u0198")
        buf.write("\3\2\2\2U\u019b\3\2\2\2W\u019d\3\2\2\2Y\u01a0\3\2\2\2")
        buf.write("[\u01a2\3\2\2\2]\u01a5\3\2\2\2_\u01a8\3\2\2\2a\u01aa\3")
        buf.write("\2\2\2c\u01ac\3\2\2\2e\u01ae\3\2\2\2g\u01b0\3\2\2\2i\u01b2")
        buf.write("\3\2\2\2k\u01b4\3\2\2\2m\u01b6\3\2\2\2o\u01b8\3\2\2\2")
        buf.write("q\u01ba\3\2\2\2s\u01bc\3\2\2\2u\u01be\3\2\2\2w\u01cc\3")
        buf.write("\2\2\2y\u01d7\3\2\2\2{\u01de\3\2\2\2}\u01e1\3\2\2\2\177")
        buf.write("\u01f9\3\2\2\2\u0081\u01fb\3\2\2\2\u0083\u0201\3\2\2\2")
        buf.write("\u0085\u0223\3\2\2\2\u0087\u0225\3\2\2\2\u0089\u0228\3")
        buf.write("\2\2\2\u008b\u022b\3\2\2\2\u008d\u022f\3\2\2\2\u008f\u0235")
        buf.write("\3\2\2\2\u0091\u0238\3\2\2\2\u0093\u0241\3\2\2\2\u0095")
        buf.write("\u0096\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098\7c\2\2\u0098")
        buf.write("\u0099\7f\2\2\u0099\u009a\7K\2\2\u009a\u009b\7p\2\2\u009b")
        buf.write("\u009c\7v\2\2\u009c\u009d\7g\2\2\u009d\u009e\7i\2\2\u009e")
        buf.write("\u009f\7g\2\2\u009f\u00a0\7t\2\2\u00a0\4\3\2\2\2\u00a1")
        buf.write("\u00a2\7r\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7k\2\2\u00a4")
        buf.write("\u00a5\7p\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7K\2\2\u00a7")
        buf.write("\u00a8\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7g\2\2\u00aa")
        buf.write("\u00ab\7i\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7t\2\2\u00ad")
        buf.write("\6\3\2\2\2\u00ae\u00af\7t\2\2\u00af\u00b0\7g\2\2\u00b0")
        buf.write("\u00b1\7c\2\2\u00b1\u00b2\7f\2\2\u00b2\u00b3\7H\2\2\u00b3")
        buf.write("\u00b4\7n\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6\7c\2\2\u00b6")
        buf.write("\u00b7\7v\2\2\u00b7\b\3\2\2\2\u00b8\u00b9\7y\2\2\u00b9")
        buf.write("\u00ba\7t\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7v\2\2\u00bc")
        buf.write("\u00bd\7g\2\2\u00bd\u00be\7H\2\2\u00be\u00bf\7n\2\2\u00bf")
        buf.write("\u00c0\7q\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7v\2\2\u00c2")
        buf.write("\n\3\2\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7g\2\2\u00c5")
        buf.write("\u00c6\7c\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8\7D\2\2\u00c8")
        buf.write("\u00c9\7q\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7n\2\2\u00cb")
        buf.write("\u00cc\7g\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7p\2\2\u00ce")
        buf.write("\f\3\2\2\2\u00cf\u00d0\7r\2\2\u00d0\u00d1\7t\2\2\u00d1")
        buf.write("\u00d2\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4")
        buf.write("\u00d5\7D\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7q\2\2\u00d7")
        buf.write("\u00d8\7n\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7c\2\2\u00da")
        buf.write("\u00db\7p\2\2\u00db\16\3\2\2\2\u00dc\u00dd\7t\2\2\u00dd")
        buf.write("\u00de\7g\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7f\2\2\u00e0")
        buf.write("\u00e1\7U\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7t\2\2\u00e3")
        buf.write("\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7i\2\2\u00e6")
        buf.write("\20\3\2\2\2\u00e7\u00e8\7r\2\2\u00e8\u00e9\7t\2\2\u00e9")
        buf.write("\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec")
        buf.write("\u00ed\7U\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7t\2\2\u00ef")
        buf.write("\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2\7i\2\2\u00f2")
        buf.write("\22\3\2\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7w\2\2\u00f5")
        buf.write("\u00f6\7r\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7t\2\2\u00f8")
        buf.write("\24\3\2\2\2\u00f9\u00fa\7r\2\2\u00fa\u00fb\7t\2\2\u00fb")
        buf.write("\u00fc\7g\2\2\u00fc\u00fd\7x\2\2\u00fd\u00fe\7g\2\2\u00fe")
        buf.write("\u00ff\7p\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7F\2\2\u0101")
        buf.write("\u0102\7g\2\2\u0102\u0103\7h\2\2\u0103\u0104\7c\2\2\u0104")
        buf.write("\u0105\7w\2\2\u0105\u0106\7n\2\2\u0106\u0107\7v\2\2\u0107")
        buf.write("\26\3\2\2\2\u0108\u0109\7c\2\2\u0109\u010a\7w\2\2\u010a")
        buf.write("\u010b\7v\2\2\u010b\u010c\7q\2\2\u010c\30\3\2\2\2\u010d")
        buf.write("\u010e\7d\2\2\u010e\u010f\7t\2\2\u010f\u0110\7g\2\2\u0110")
        buf.write("\u0111\7c\2\2\u0111\u0112\7m\2\2\u0112\32\3\2\2\2\u0113")
        buf.write("\u0114\7d\2\2\u0114\u0115\7q\2\2\u0115\u0116\7q\2\2\u0116")
        buf.write("\u0117\7n\2\2\u0117\u0118\7g\2\2\u0118\u0119\7c\2\2\u0119")
        buf.write("\u011a\7p\2\2\u011a\34\3\2\2\2\u011b\u011c\7f\2\2\u011c")
        buf.write("\u011d\7q\2\2\u011d\36\3\2\2\2\u011e\u011f\7g\2\2\u011f")
        buf.write("\u0120\7n\2\2\u0120\u0121\7u\2\2\u0121\u0122\7g\2\2\u0122")
        buf.write(" \3\2\2\2\u0123\u0124\7h\2\2\u0124\u0125\7c\2\2\u0125")
        buf.write("\u0126\7n\2\2\u0126\u0127\7u\2\2\u0127\u0128\7g\2\2\u0128")
        buf.write("\"\3\2\2\2\u0129\u012a\7h\2\2\u012a\u012b\7n\2\2\u012b")
        buf.write("\u012c\7q\2\2\u012c\u012d\7c\2\2\u012d\u012e\7v\2\2\u012e")
        buf.write("$\3\2\2\2\u012f\u0130\7h\2\2\u0130\u0131\7q\2\2\u0131")
        buf.write("\u0132\7t\2\2\u0132&\3\2\2\2\u0133\u0134\7h\2\2\u0134")
        buf.write("\u0135\7w\2\2\u0135\u0136\7p\2\2\u0136\u0137\7e\2\2\u0137")
        buf.write("\u0138\7v\2\2\u0138\u0139\7k\2\2\u0139\u013a\7q\2\2\u013a")
        buf.write("\u013b\7p\2\2\u013b(\3\2\2\2\u013c\u013d\7k\2\2\u013d")
        buf.write("\u013e\7h\2\2\u013e*\3\2\2\2\u013f\u0140\7k\2\2\u0140")
        buf.write("\u0141\7p\2\2\u0141\u0142\7v\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write("\u0144\7i\2\2\u0144\u0145\7g\2\2\u0145\u0146\7t\2\2\u0146")
        buf.write(",\3\2\2\2\u0147\u0148\7t\2\2\u0148\u0149\7g\2\2\u0149")
        buf.write("\u014a\7v\2\2\u014a\u014b\7w\2\2\u014b\u014c\7t\2\2\u014c")
        buf.write("\u014d\7p\2\2\u014d.\3\2\2\2\u014e\u014f\7u\2\2\u014f")
        buf.write("\u0150\7v\2\2\u0150\u0151\7t\2\2\u0151\u0152\7k\2\2\u0152")
        buf.write("\u0153\7p\2\2\u0153\u0154\7i\2\2\u0154\60\3\2\2\2\u0155")
        buf.write("\u0156\7v\2\2\u0156\u0157\7t\2\2\u0157\u0158\7w\2\2\u0158")
        buf.write("\u0159\7g\2\2\u0159\62\3\2\2\2\u015a\u015b\7y\2\2\u015b")
        buf.write("\u015c\7j\2\2\u015c\u015d\7k\2\2\u015d\u015e\7n\2\2\u015e")
        buf.write("\u015f\7g\2\2\u015f\64\3\2\2\2\u0160\u0161\7x\2\2\u0161")
        buf.write("\u0162\7q\2\2\u0162\u0163\7k\2\2\u0163\u0164\7f\2\2\u0164")
        buf.write("\66\3\2\2\2\u0165\u0166\7q\2\2\u0166\u0167\7w\2\2\u0167")
        buf.write("\u0168\7v\2\2\u01688\3\2\2\2\u0169\u016a\7e\2\2\u016a")
        buf.write("\u016b\7q\2\2\u016b\u016c\7p\2\2\u016c\u016d\7v\2\2\u016d")
        buf.write("\u016e\7k\2\2\u016e\u016f\7p\2\2\u016f\u0170\7w\2\2\u0170")
        buf.write("\u0171\7g\2\2\u0171:\3\2\2\2\u0172\u0173\7q\2\2\u0173")
        buf.write("\u0174\7h\2\2\u0174<\3\2\2\2\u0175\u0176\7k\2\2\u0176")
        buf.write("\u0177\7p\2\2\u0177\u0178\7j\2\2\u0178\u0179\7g\2\2\u0179")
        buf.write("\u017a\7t\2\2\u017a\u017b\7k\2\2\u017b\u017c\7v\2\2\u017c")
        buf.write(">\3\2\2\2\u017d\u017e\7c\2\2\u017e\u017f\7t\2\2\u017f")
        buf.write("\u0180\7t\2\2\u0180\u0181\7c\2\2\u0181\u0182\7{\2\2\u0182")
        buf.write("@\3\2\2\2\u0183\u0184\7-\2\2\u0184B\3\2\2\2\u0185\u0186")
        buf.write("\7/\2\2\u0186D\3\2\2\2\u0187\u0188\7,\2\2\u0188F\3\2\2")
        buf.write("\2\u0189\u018a\7\61\2\2\u018aH\3\2\2\2\u018b\u018c\7\'")
        buf.write("\2\2\u018cJ\3\2\2\2\u018d\u018e\7#\2\2\u018eL\3\2\2\2")
        buf.write("\u018f\u0190\7(\2\2\u0190\u0191\7(\2\2\u0191N\3\2\2\2")
        buf.write("\u0192\u0193\7~\2\2\u0193\u0194\7~\2\2\u0194P\3\2\2\2")
        buf.write("\u0195\u0196\7?\2\2\u0196\u0197\7?\2\2\u0197R\3\2\2\2")
        buf.write("\u0198\u0199\7#\2\2\u0199\u019a\7?\2\2\u019aT\3\2\2\2")
        buf.write("\u019b\u019c\7>\2\2\u019cV\3\2\2\2\u019d\u019e\7>\2\2")
        buf.write("\u019e\u019f\7?\2\2\u019fX\3\2\2\2\u01a0\u01a1\7@\2\2")
        buf.write("\u01a1Z\3\2\2\2\u01a2\u01a3\7@\2\2\u01a3\u01a4\7?\2\2")
        buf.write("\u01a4\\\3\2\2\2\u01a5\u01a6\7<\2\2\u01a6\u01a7\7<\2\2")
        buf.write("\u01a7^\3\2\2\2\u01a8\u01a9\7*\2\2\u01a9`\3\2\2\2\u01aa")
        buf.write("\u01ab\7+\2\2\u01abb\3\2\2\2\u01ac\u01ad\7]\2\2\u01ad")
        buf.write("d\3\2\2\2\u01ae\u01af\7_\2\2\u01aff\3\2\2\2\u01b0\u01b1")
        buf.write("\7\60\2\2\u01b1h\3\2\2\2\u01b2\u01b3\7.\2\2\u01b3j\3\2")
        buf.write("\2\2\u01b4\u01b5\7=\2\2\u01b5l\3\2\2\2\u01b6\u01b7\7<")
        buf.write("\2\2\u01b7n\3\2\2\2\u01b8\u01b9\7}\2\2\u01b9p\3\2\2\2")
        buf.write("\u01ba\u01bb\7\177\2\2\u01bbr\3\2\2\2\u01bc\u01bd\7?\2")
        buf.write("\2\u01bdt\3\2\2\2\u01be\u01bf\7\61\2\2\u01bf\u01c0\7,")
        buf.write("\2\2\u01c0\u01c4\3\2\2\2\u01c1\u01c3\13\2\2\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c7\u01c8\7,\2\2\u01c8\u01c9\7\61\2\2\u01c9\u01ca\3")
        buf.write("\2\2\2\u01ca\u01cb\b;\2\2\u01cbv\3\2\2\2\u01cc\u01cd\7")
        buf.write("\61\2\2\u01cd\u01ce\7\61\2\2\u01ce\u01d2\3\2\2\2\u01cf")
        buf.write("\u01d1\n\2\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d4\3\2\2\2")
        buf.write("\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5\3")
        buf.write("\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d6\b<\2\2\u01d6x\3")
        buf.write("\2\2\2\u01d7\u01db\t\3\2\2\u01d8\u01da\t\4\2\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dcz\3\2\2\2\u01dd\u01db\3\2\2\2\u01de")
        buf.write("\u01df\5\177@\2\u01df\u01e0\b>\3\2\u01e0|\3\2\2\2\u01e1")
        buf.write("\u01e3\5\177@\2\u01e2\u01e4\5\u0081A\2\u01e3\u01e2\3\2")
        buf.write("\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e6\3\2\2\2\u01e5\u01e7")
        buf.write("\5\u0083B\2\u01e6\u01e5\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u01e9\b?\4\2\u01e9~\3\2\2\2\u01ea")
        buf.write("\u01fa\7\62\2\2\u01eb\u01f6\t\5\2\2\u01ec\u01ee\7a\2\2")
        buf.write("\u01ed\u01ec\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f0\3")
        buf.write("\2\2\2\u01ef\u01f1\t\6\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01f2")
        buf.write("\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("\u01f5\3\2\2\2\u01f4\u01ed\3\2\2\2\u01f5\u01f8\3\2\2\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01fa\3")
        buf.write("\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01ea\3\2\2\2\u01f9\u01eb")
        buf.write("\3\2\2\2\u01fa\u0080\3\2\2\2\u01fb\u01fd\7\60\2\2\u01fc")
        buf.write("\u01fe\t\6\2\2\u01fd\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2")
        buf.write("\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0082\3")
        buf.write("\2\2\2\u0201\u0203\t\7\2\2\u0202\u0204\t\b\2\2\u0203\u0202")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205")
        buf.write("\u0207\t\6\2\2\u0206\u0205\3\2\2\2\u0207\u0208\3\2\2\2")
        buf.write("\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u0084\3")
        buf.write("\2\2\2\u020a\u020b\7$\2\2\u020b\u0224\7$\2\2\u020c\u021d")
        buf.write("\7$\2\2\u020d\u021c\n\t\2\2\u020e\u020f\7^\2\2\u020f\u021c")
        buf.write("\7v\2\2\u0210\u0211\7^\2\2\u0211\u021c\7t\2\2\u0212\u0213")
        buf.write("\7^\2\2\u0213\u021c\7p\2\2\u0214\u0215\7^\2\2\u0215\u021c")
        buf.write("\7d\2\2\u0216\u0217\7^\2\2\u0217\u021c\7h\2\2\u0218\u021c")
        buf.write("\5\u0087D\2\u0219\u021c\5\u0089E\2\u021a\u021c\5\u008b")
        buf.write("F\2\u021b\u020d\3\2\2\2\u021b\u020e\3\2\2\2\u021b\u0210")
        buf.write("\3\2\2\2\u021b\u0212\3\2\2\2\u021b\u0214\3\2\2\2\u021b")
        buf.write("\u0216\3\2\2\2\u021b\u0218\3\2\2\2\u021b\u0219\3\2\2\2")
        buf.write("\u021b\u021a\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021d\u021e\3\2\2\2\u021e\u0220\3\2\2\2\u021f\u021d")
        buf.write("\3\2\2\2\u0220\u0221\n\n\2\2\u0221\u0222\7$\2\2\u0222")
        buf.write("\u0224\bC\5\2\u0223\u020a\3\2\2\2\u0223\u020c\3\2\2\2")
        buf.write("\u0224\u0086\3\2\2\2\u0225\u0226\7^\2\2\u0226\u0227\7")
        buf.write(")\2\2\u0227\u0088\3\2\2\2\u0228\u0229\7^\2\2\u0229\u022a")
        buf.write("\7$\2\2\u022a\u008a\3\2\2\2\u022b\u022c\7^\2\2\u022c\u022d")
        buf.write("\7^\2\2\u022d\u008c\3\2\2\2\u022e\u0230\t\13\2\2\u022f")
        buf.write("\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0231\u0232\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234\b")
        buf.write("G\2\2\u0234\u008e\3\2\2\2\u0235\u0236\13\2\2\2\u0236\u0237")
        buf.write("\bH\6\2\u0237\u0090\3\2\2\2\u0238\u023c\7$\2\2\u0239\u023b")
        buf.write("\n\f\2\2\u023a\u0239\3\2\2\2\u023b\u023e\3\2\2\2\u023c")
        buf.write("\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023f\3\2\2\2")
        buf.write("\u023e\u023c\3\2\2\2\u023f\u0240\bI\7\2\u0240\u0092\3")
        buf.write("\2\2\2\u0241\u0245\7$\2\2\u0242\u0244\13\2\2\2\u0243\u0242")
        buf.write("\3\2\2\2\u0244\u0247\3\2\2\2\u0245\u0246\3\2\2\2\u0245")
        buf.write("\u0243\3\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245\3\2\2\2")
        buf.write("\u0248\u024a\t\r\2\2\u0249\u0248\3\2\2\2\u024a\u024e\3")
        buf.write("\2\2\2\u024b\u024d\13\2\2\2\u024c\u024b\3\2\2\2\u024d")
        buf.write("\u0250\3\2\2\2\u024e\u024f\3\2\2\2\u024e\u024c\3\2\2\2")
        buf.write("\u024f\u0251\3\2\2\2\u0250\u024e\3\2\2\2\u0251\u0252\7")
        buf.write("$\2\2\u0252\u0253\bJ\b\2\u0253\u0094\3\2\2\2\27\2\u01c4")
        buf.write("\u01d2\u01db\u01e3\u01e6\u01ed\u01f2\u01f6\u01f9\u01ff")
        buf.write("\u0203\u0208\u021b\u021d\u0223\u0231\u023c\u0245\u0249")
        buf.write("\u024e\t\b\2\2\3>\2\3?\3\3C\4\3H\5\3I\6\3J\7")
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
    SUPER = 9
    PREVENT_DEF = 10
    AUTO = 11
    BREAK = 12
    BOOLEAN = 13
    DO = 14
    ELSE = 15
    FALSE = 16
    FLOAT = 17
    FOR = 18
    FUNCTION = 19
    IF = 20
    INTEGER = 21
    RETURN = 22
    STRING = 23
    TRUE = 24
    WHILE = 25
    VOID = 26
    OUT = 27
    CONTINUE = 28
    OF = 29
    INHERIT = 30
    ARRAY = 31
    ADDOP = 32
    SUBOP = 33
    MULOP = 34
    DIVOP = 35
    MODULO = 36
    LOGICNOT = 37
    AND = 38
    OR = 39
    EQ = 40
    NOTEQ = 41
    LESS = 42
    LESSOREQ = 43
    MORE_ = 44
    MOREOREQ = 45
    DBLCOL = 46
    LP = 47
    RP = 48
    LSB = 49
    RSB = 50
    DOT = 51
    COMMA = 52
    SEMI = 53
    COLON = 54
    LCB = 55
    RCB = 56
    ASSIGN = 57
    COMMENT = 58
    LINE_COMMENT = 59
    ID = 60
    INT_TYPE = 61
    FLOAT_TYPE = 62
    STRING_TYPE = 63
    WS = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'auto'", "'break'", "'boolean'", 
            "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
            "'if'", "'integer'", "'return'", "'string'", "'true'", "'while'", 
            "'void'", "'out'", "'continue'", "'of'", "'inherit'", "'array'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "READ_INT", "PRINT_INT", "READ_FLOAT", "WRITE_FLOAT", "READ_BOOL", 
            "PRINT_BOOL", "READ_STR", "PRINT_STR", "SUPER", "PREVENT_DEF", 
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODULO", "LOGICNOT", "AND", 
            "OR", "EQ", "NOTEQ", "LESS", "LESSOREQ", "MORE_", "MOREOREQ", 
            "DBLCOL", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", 
            "COLON", "LCB", "RCB", "ASSIGN", "COMMENT", "LINE_COMMENT", 
            "ID", "INT_TYPE", "FLOAT_TYPE", "STRING_TYPE", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "READ_INT", "PRINT_INT", "READ_FLOAT", "WRITE_FLOAT", 
                  "READ_BOOL", "PRINT_BOOL", "READ_STR", "PRINT_STR", "SUPER", 
                  "PREVENT_DEF", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                  "MODULO", "LOGICNOT", "AND", "OR", "EQ", "NOTEQ", "LESS", 
                  "LESSOREQ", "MORE_", "MOREOREQ", "DBLCOL", "LP", "RP", 
                  "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "LCB", 
                  "RCB", "ASSIGN", "COMMENT", "LINE_COMMENT", "ID", "INT_TYPE", 
                  "FLOAT_TYPE", "INTPART", "DECIMAL", "EXPONENT", "STRING_TYPE", 
                  "QUOTE", "DBLQUOTE", "BACKSLASH", "WS", "ERROR_CHAR", 
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
            actions[60] = self.INT_TYPE_action 
            actions[61] = self.FLOAT_TYPE_action 
            actions[65] = self.STRING_TYPE_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
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
     


