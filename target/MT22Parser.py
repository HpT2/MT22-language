# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u018c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3Y\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4a\n\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4h\n\4\3\5\3\5\3\5\5\5m\n\5\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6t\n\6\3\7\3\7\3\7\3\7\5\7z\n\7\3\7\3\7\3\7\3\7\7\7\u0080")
        buf.write("\n\7\f\7\16\7\u0083\13\7\3\b\3\b\3\b\3\b\3\b\5\b\u008a")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u009a\n\n\3\13\3\13\3\13\3\13\3\13\3\13\7\13")
        buf.write("\u00a2\n\13\f\13\16\13\u00a5\13\13\3\f\3\f\3\r\3\r\3\r")
        buf.write("\5\r\u00ac\n\r\3\r\3\r\3\r\3\r\7\r\u00b2\n\r\f\r\16\r")
        buf.write("\u00b5\13\r\3\16\3\16\3\16\5\16\u00ba\n\16\3\16\3\16\3")
        buf.write("\16\3\16\7\16\u00c0\n\16\f\16\16\16\u00c3\13\16\3\17\3")
        buf.write("\17\3\17\5\17\u00c8\n\17\3\17\3\17\3\17\7\17\u00cd\n\17")
        buf.write("\f\17\16\17\u00d0\13\17\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u00d9\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00e3\n\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f3\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00fe\n\25\3\26\3\26\3\26\3\26\5\26\u0104\n\26\3\27\3")
        buf.write("\27\5\27\u0108\n\27\3\30\5\30\u010b\n\30\3\30\5\30\u010e")
        buf.write("\n\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u0119\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0122")
        buf.write("\n\32\3\32\3\32\3\32\5\32\u0127\n\32\3\32\3\32\3\32\3")
        buf.write("\32\3\33\3\33\5\33\u012f\n\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0147\n\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \5 \u0151\n \3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3$\3$\3$\3$\3$\5$\u0171\n$\3%\3%\3%\3%\3%\5%\u0178\n")
        buf.write("%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0184\n&\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\2\7\f\24\30\32\34)\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLN\2")
        buf.write("\6\3\2\35%\5\2\b\b\20\20\64\67\6\2\5\5\t\t\r\r\17\17\3")
        buf.write("\2\30\34\2\u0197\2P\3\2\2\2\4X\3\2\2\2\6g\3\2\2\2\bl\3")
        buf.write("\2\2\2\ns\3\2\2\2\fy\3\2\2\2\16\u0089\3\2\2\2\20\u008b")
        buf.write("\3\2\2\2\22\u0099\3\2\2\2\24\u009b\3\2\2\2\26\u00a6\3")
        buf.write("\2\2\2\30\u00ab\3\2\2\2\32\u00b9\3\2\2\2\34\u00c7\3\2")
        buf.write("\2\2\36\u00d1\3\2\2\2 \u00d3\3\2\2\2\"\u00dd\3\2\2\2$")
        buf.write("\u00f2\3\2\2\2&\u00f4\3\2\2\2(\u00fd\3\2\2\2*\u0103\3")
        buf.write("\2\2\2,\u0107\3\2\2\2.\u010a\3\2\2\2\60\u0118\3\2\2\2")
        buf.write("\62\u011a\3\2\2\2\64\u012e\3\2\2\2\66\u0130\3\2\2\28\u0134")
        buf.write("\3\2\2\2:\u0137\3\2\2\2<\u0146\3\2\2\2>\u0148\3\2\2\2")
        buf.write("@\u0152\3\2\2\2B\u015e\3\2\2\2D\u0164\3\2\2\2F\u0170\3")
        buf.write("\2\2\2H\u0177\3\2\2\2J\u0183\3\2\2\2L\u0185\3\2\2\2N\u0189")
        buf.write("\3\2\2\2PQ\5\4\3\2QR\7\2\2\3R\3\3\2\2\2ST\5\6\4\2TU\5")
        buf.write("\4\3\2UY\3\2\2\2VY\5\6\4\2WY\3\2\2\2XS\3\2\2\2XV\3\2\2")
        buf.write("\2XW\3\2\2\2Y\5\3\2\2\2Zh\5\b\5\2[h\5L\'\2\\a\5\66\34")
        buf.write("\2]a\58\35\2^a\5:\36\2_a\5D#\2`\\\3\2\2\2`]\3\2\2\2`^")
        buf.write("\3\2\2\2`_\3\2\2\2ab\3\2\2\2bc\7-\2\2ch\3\2\2\2dh\5> ")
        buf.write("\2eh\5@!\2fh\5B\"\2gZ\3\2\2\2g[\3\2\2\2g`\3\2\2\2gd\3")
        buf.write("\2\2\2ge\3\2\2\2gf\3\2\2\2h\7\3\2\2\2im\5 \21\2jm\5\62")
        buf.write("\32\2km\5\"\22\2li\3\2\2\2lj\3\2\2\2lk\3\2\2\2m\t\3\2")
        buf.write("\2\2nt\5\f\7\2ot\5\34\17\2pt\5\24\13\2qt\5:\36\2rt\5\20")
        buf.write("\t\2sn\3\2\2\2so\3\2\2\2sp\3\2\2\2sq\3\2\2\2sr\3\2\2\2")
        buf.write("t\13\3\2\2\2uv\b\7\1\2vz\5\30\r\2wz\5\32\16\2xz\5:\36")
        buf.write("\2yu\3\2\2\2yw\3\2\2\2yx\3\2\2\2z\u0081\3\2\2\2{|\f\6")
        buf.write("\2\2|}\5N(\2}~\5\f\7\7~\u0080\3\2\2\2\177{\3\2\2\2\u0080")
        buf.write("\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\r\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\5\n\6\2\u0085")
        buf.write("\u0086\7,\2\2\u0086\u0087\5\16\b\2\u0087\u008a\3\2\2\2")
        buf.write("\u0088\u008a\5\n\6\2\u0089\u0084\3\2\2\2\u0089\u0088\3")
        buf.write("\2\2\2\u008a\17\3\2\2\2\u008b\u008c\7\64\2\2\u008c\u008d")
        buf.write("\7)\2\2\u008d\u008e\5\22\n\2\u008e\u008f\7*\2\2\u008f")
        buf.write("\21\3\2\2\2\u0090\u0091\5\30\r\2\u0091\u0092\7,\2\2\u0092")
        buf.write("\u0093\5\22\n\2\u0093\u009a\3\2\2\2\u0094\u0095\5\20\t")
        buf.write("\2\u0095\u0096\7,\2\2\u0096\u0097\5\22\n\2\u0097\u009a")
        buf.write("\3\2\2\2\u0098\u009a\5\20\t\2\u0099\u0090\3\2\2\2\u0099")
        buf.write("\u0094\3\2\2\2\u0099\u0098\3\2\2\2\u009a\23\3\2\2\2\u009b")
        buf.write("\u009c\b\13\1\2\u009c\u009d\5\26\f\2\u009d\u00a3\3\2\2")
        buf.write("\2\u009e\u009f\f\4\2\2\u009f\u00a0\t\2\2\2\u00a0\u00a2")
        buf.write("\5\24\13\5\u00a1\u009e\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\25\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a6\u00a7\t\3\2\2\u00a7\27\3\2\2\2\u00a8")
        buf.write("\u00a9\b\r\1\2\u00a9\u00ac\7\65\2\2\u00aa\u00ac\7\64\2")
        buf.write("\2\u00ab\u00a8\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00b3")
        buf.write("\3\2\2\2\u00ad\u00ae\f\5\2\2\u00ae\u00af\5N(\2\u00af\u00b0")
        buf.write("\5\30\r\6\u00b0\u00b2\3\2\2\2\u00b1\u00ad\3\2\2\2\u00b2")
        buf.write("\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\31\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\b\16")
        buf.write("\1\2\u00b7\u00ba\7\66\2\2\u00b8\u00ba\7\64\2\2\u00b9\u00b6")
        buf.write("\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00c1\3\2\2\2\u00bb")
        buf.write("\u00bc\f\5\2\2\u00bc\u00bd\5N(\2\u00bd\u00be\5\32\16\6")
        buf.write("\u00be\u00c0\3\2\2\2\u00bf\u00bb\3\2\2\2\u00c0\u00c3\3")
        buf.write("\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\33")
        buf.write("\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5\b\17\1\2\u00c5")
        buf.write("\u00c8\7\67\2\2\u00c6\u00c8\7\64\2\2\u00c7\u00c4\3\2\2")
        buf.write("\2\u00c7\u00c6\3\2\2\2\u00c8\u00ce\3\2\2\2\u00c9\u00ca")
        buf.write("\f\5\2\2\u00ca\u00cb\7&\2\2\u00cb\u00cd\5\34\17\6\u00cc")
        buf.write("\u00c9\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\35\3\2\2\2\u00d0\u00ce\3\2")
        buf.write("\2\2\u00d1\u00d2\t\4\2\2\u00d2\37\3\2\2\2\u00d3\u00d4")
        buf.write("\5*\26\2\u00d4\u00d5\7.\2\2\u00d5\u00d8\5\36\20\2\u00d6")
        buf.write("\u00d7\7\61\2\2\u00d7\u00d9\5\16\b\2\u00d8\u00d6\3\2\2")
        buf.write("\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db")
        buf.write("\7-\2\2\u00db\u00dc\b\21\1\2\u00dc!\3\2\2\2\u00dd\u00de")
        buf.write("\5*\26\2\u00de\u00df\7.\2\2\u00df\u00e2\7\27\2\2\u00e0")
        buf.write("\u00e1\7\61\2\2\u00e1\u00e3\5$\23\2\u00e2\u00e0\3\2\2")
        buf.write("\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5")
        buf.write("\7-\2\2\u00e5#\3\2\2\2\u00e6\u00e7\7\27\2\2\u00e7\u00e8")
        buf.write("\5&\24\2\u00e8\u00e9\7\25\2\2\u00e9\u00ea\5\36\20\2\u00ea")
        buf.write("\u00eb\7,\2\2\u00eb\u00ec\5$\23\2\u00ec\u00f3\3\2\2\2")
        buf.write("\u00ed\u00ee\7\27\2\2\u00ee\u00ef\5&\24\2\u00ef\u00f0")
        buf.write("\7\25\2\2\u00f0\u00f1\5\36\20\2\u00f1\u00f3\3\2\2\2\u00f2")
        buf.write("\u00e6\3\2\2\2\u00f2\u00ed\3\2\2\2\u00f3%\3\2\2\2\u00f4")
        buf.write("\u00f5\7)\2\2\u00f5\u00f6\5(\25\2\u00f6\u00f7\7*\2\2\u00f7")
        buf.write("\'\3\2\2\2\u00f8\u00f9\5\30\r\2\u00f9\u00fa\7,\2\2\u00fa")
        buf.write("\u00fb\5(\25\2\u00fb\u00fe\3\2\2\2\u00fc\u00fe\5\30\r")
        buf.write("\2\u00fd\u00f8\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe)\3\2")
        buf.write("\2\2\u00ff\u0100\7\64\2\2\u0100\u0101\7,\2\2\u0101\u0104")
        buf.write("\5*\26\2\u0102\u0104\7\64\2\2\u0103\u00ff\3\2\2\2\u0103")
        buf.write("\u0102\3\2\2\2\u0104+\3\2\2\2\u0105\u0108\5\36\20\2\u0106")
        buf.write("\u0108\7\22\2\2\u0107\u0105\3\2\2\2\u0107\u0106\3\2\2")
        buf.write("\2\u0108-\3\2\2\2\u0109\u010b\7\26\2\2\u010a\u0109\3\2")
        buf.write("\2\2\u010a\u010b\3\2\2\2\u010b\u010d\3\2\2\2\u010c\u010e")
        buf.write("\7\23\2\2\u010d\u010c\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0110\7\64\2\2\u0110\u0111\7.\2\2")
        buf.write("\u0111\u0112\5\36\20\2\u0112/\3\2\2\2\u0113\u0114\5.\30")
        buf.write("\2\u0114\u0115\7,\2\2\u0115\u0116\5\60\31\2\u0116\u0119")
        buf.write("\3\2\2\2\u0117\u0119\5.\30\2\u0118\u0113\3\2\2\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119\61\3\2\2\2\u011a\u011b\7\64\2\2\u011b")
        buf.write("\u011c\7.\2\2\u011c\u011d\7\13\2\2\u011d\u011e\5,\27\2")
        buf.write("\u011e\u0121\7\'\2\2\u011f\u0122\5\60\31\2\u0120\u0122")
        buf.write("\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\u0123\3\2\2\2\u0123\u0126\7(\2\2\u0124\u0125\7\26\2\2")
        buf.write("\u0125\u0127\7\64\2\2\u0126\u0124\3\2\2\2\u0126\u0127")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\7/\2\2\u0129")
        buf.write("\u012a\5\64\33\2\u012a\u012b\7\60\2\2\u012b\63\3\2\2\2")
        buf.write("\u012c\u012f\5\4\3\2\u012d\u012f\3\2\2\2\u012e\u012c\3")
        buf.write("\2\2\2\u012e\u012d\3\2\2\2\u012f\65\3\2\2\2\u0130\u0131")
        buf.write("\7\64\2\2\u0131\u0132\7\61\2\2\u0132\u0133\5\n\6\2\u0133")
        buf.write("\67\3\2\2\2\u0134\u0135\7\16\2\2\u0135\u0136\5\n\6\2\u0136")
        buf.write("9\3\2\2\2\u0137\u0138\7\64\2\2\u0138\u0139\7\'\2\2\u0139")
        buf.write("\u013a\5<\37\2\u013a\u013b\7(\2\2\u013b;\3\2\2\2\u013c")
        buf.write("\u013d\7\64\2\2\u013d\u013e\7,\2\2\u013e\u0147\5<\37\2")
        buf.write("\u013f\u0140\5\n\6\2\u0140\u0141\7,\2\2\u0141\u0142\5")
        buf.write("<\37\2\u0142\u0147\3\2\2\2\u0143\u0147\7\64\2\2\u0144")
        buf.write("\u0147\5\n\6\2\u0145\u0147\3\2\2\2\u0146\u013c\3\2\2\2")
        buf.write("\u0146\u013f\3\2\2\2\u0146\u0143\3\2\2\2\u0146\u0144\3")
        buf.write("\2\2\2\u0146\u0145\3\2\2\2\u0147=\3\2\2\2\u0148\u0149")
        buf.write("\7\f\2\2\u0149\u014a\7\'\2\2\u014a\u014b\5\24\13\2\u014b")
        buf.write("\u014c\7(\2\2\u014c\u0150\5F$\2\u014d\u014e\7\7\2\2\u014e")
        buf.write("\u0151\5F$\2\u014f\u0151\3\2\2\2\u0150\u014d\3\2\2\2\u0150")
        buf.write("\u014f\3\2\2\2\u0151?\3\2\2\2\u0152\u0153\7\n\2\2\u0153")
        buf.write("\u0154\7\'\2\2\u0154\u0155\7\64\2\2\u0155\u0156\7\61\2")
        buf.write("\2\u0156\u0157\5\30\r\2\u0157\u0158\7,\2\2\u0158\u0159")
        buf.write("\5\24\13\2\u0159\u015a\7,\2\2\u015a\u015b\5\30\r\2\u015b")
        buf.write("\u015c\7(\2\2\u015c\u015d\5H%\2\u015dA\3\2\2\2\u015e\u015f")
        buf.write("\7\21\2\2\u015f\u0160\7\'\2\2\u0160\u0161\5\24\13\2\u0161")
        buf.write("\u0162\7(\2\2\u0162\u0163\5H%\2\u0163C\3\2\2\2\u0164\u0165")
        buf.write("\7\6\2\2\u0165\u0166\5H%\2\u0166\u0167\7\21\2\2\u0167")
        buf.write("\u0168\7\'\2\2\u0168\u0169\5\24\13\2\u0169\u016a\7(\2")
        buf.write("\2\u016aE\3\2\2\2\u016b\u0171\5\6\4\2\u016c\u016d\7/\2")
        buf.write("\2\u016d\u016e\5\4\3\2\u016e\u016f\7\60\2\2\u016f\u0171")
        buf.write("\3\2\2\2\u0170\u016b\3\2\2\2\u0170\u016c\3\2\2\2\u0171")
        buf.write("G\3\2\2\2\u0172\u0178\5\6\4\2\u0173\u0174\7/\2\2\u0174")
        buf.write("\u0175\5J&\2\u0175\u0176\7\60\2\2\u0176\u0178\3\2\2\2")
        buf.write("\u0177\u0172\3\2\2\2\u0177\u0173\3\2\2\2\u0178I\3\2\2")
        buf.write("\2\u0179\u017a\5\6\4\2\u017a\u017b\5J&\2\u017b\u0184\3")
        buf.write("\2\2\2\u017c\u017d\7\4\2\2\u017d\u017e\7-\2\2\u017e\u0184")
        buf.write("\5J&\2\u017f\u0180\7\24\2\2\u0180\u0181\7-\2\2\u0181\u0184")
        buf.write("\5J&\2\u0182\u0184\3\2\2\2\u0183\u0179\3\2\2\2\u0183\u017c")
        buf.write("\3\2\2\2\u0183\u017f\3\2\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("K\3\2\2\2\u0185\u0186\7/\2\2\u0186\u0187\5\4\3\2\u0187")
        buf.write("\u0188\7\60\2\2\u0188M\3\2\2\2\u0189\u018a\t\5\2\2\u018a")
        buf.write("O\3\2\2\2#X`glsy\u0081\u0089\u0099\u00a3\u00ab\u00b3\u00b9")
        buf.write("\u00c1\u00c7\u00ce\u00d8\u00e2\u00f2\u00fd\u0103\u0107")
        buf.write("\u010a\u010d\u0118\u0121\u0126\u012e\u0146\u0150\u0170")
        buf.write("\u0177\u0183")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'boolean'", "'do'", 
                     "'else'", "'false'", "'float'", "'for'", "'function'", 
                     "'if'", "'integer'", "'return'", "'string'", "'true'", 
                     "'while'", "'void'", "'out'", "'continue'", "'of'", 
                     "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", 
                     "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                      "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                      "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", 
                      "CONTINUE", "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", 
                      "MULOP", "DIVOP", "MODULO", "LOGICNOT", "AND", "OR", 
                      "EQ", "NOTEQ", "LESS", "LESSOREQ", "MORE_", "MOREOREQ", 
                      "DBLCOL", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", 
                      "SEMI", "COLON", "LCB", "RCB", "ASSIGN", "COMMENT", 
                      "LINE_COMMENT", "ID", "INT_TYPE", "FLOAT_TYPE", "STRING_TYPE", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_stmtlist = 1
    RULE_stmt = 2
    RULE_declaration = 3
    RULE_expr = 4
    RULE_numexpr = 5
    RULE_exprlist = 6
    RULE_access = 7
    RULE_accesslist = 8
    RULE_boolexpr = 9
    RULE_value = 10
    RULE_integerexpr = 11
    RULE_floatexpr = 12
    RULE_stringexpr = 13
    RULE_type_ = 14
    RULE_var_declare = 15
    RULE_array_var_decl = 16
    RULE_arraylist = 17
    RULE_dimension = 18
    RULE_intlist = 19
    RULE_id_list = 20
    RULE_function_type = 21
    RULE_param = 22
    RULE_param_list = 23
    RULE_func_declare = 24
    RULE_body = 25
    RULE_assignment = 26
    RULE_return_stmt = 27
    RULE_call_stmt = 28
    RULE_argument = 29
    RULE_if_stmt = 30
    RULE_for_stmt = 31
    RULE_while_stmt = 32
    RULE_do_while_stmt = 33
    RULE_if_body = 34
    RULE_loop_body = 35
    RULE_loop = 36
    RULE_block_stmt = 37
    RULE_numop = 38

    ruleNames =  [ "program", "stmtlist", "stmt", "declaration", "expr", 
                   "numexpr", "exprlist", "access", "accesslist", "boolexpr", 
                   "value", "integerexpr", "floatexpr", "stringexpr", "type_", 
                   "var_declare", "array_var_decl", "arraylist", "dimension", 
                   "intlist", "id_list", "function_type", "param", "param_list", 
                   "func_declare", "body", "assignment", "return_stmt", 
                   "call_stmt", "argument", "if_stmt", "for_stmt", "while_stmt", 
                   "do_while_stmt", "if_body", "loop_body", "loop", "block_stmt", 
                   "numop" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    BOOLEAN=3
    DO=4
    ELSE=5
    FALSE=6
    FLOAT=7
    FOR=8
    FUNCTION=9
    IF=10
    INTEGER=11
    RETURN=12
    STRING=13
    TRUE=14
    WHILE=15
    VOID=16
    OUT=17
    CONTINUE=18
    OF=19
    INHERIT=20
    ARRAY=21
    ADDOP=22
    SUBOP=23
    MULOP=24
    DIVOP=25
    MODULO=26
    LOGICNOT=27
    AND=28
    OR=29
    EQ=30
    NOTEQ=31
    LESS=32
    LESSOREQ=33
    MORE_=34
    MOREOREQ=35
    DBLCOL=36
    LP=37
    RP=38
    LSB=39
    RSB=40
    DOT=41
    COMMA=42
    SEMI=43
    COLON=44
    LCB=45
    RCB=46
    ASSIGN=47
    COMMENT=48
    LINE_COMMENT=49
    ID=50
    INT_TYPE=51
    FLOAT_TYPE=52
    STRING_TYPE=53
    WS=54
    ERROR_CHAR=55
    UNCLOSE_STRING=56
    ILLEGAL_ESCAPE=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.stmtlist()
            self.state = 79
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = MT22Parser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmtlist)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.stmt()
                self.state = 82
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MT22Parser.DeclarationContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def assignment(self):
            return self.getTypedRuleContext(MT22Parser.AssignmentContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Call_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Do_while_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MT22Parser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MT22Parser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.While_stmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 90
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 91
                    self.return_stmt()
                    pass

                elif la_ == 3:
                    self.state = 92
                    self.call_stmt()
                    pass

                elif la_ == 4:
                    self.state = 93
                    self.do_while_stmt()
                    pass


                self.state = 96
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 100
                self.while_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(MT22Parser.Var_declareContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(MT22Parser.Func_declareContext,0)


        def array_var_decl(self):
            return self.getTypedRuleContext(MT22Parser.Array_var_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MT22Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.func_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.array_var_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numexpr(self):
            return self.getTypedRuleContext(MT22Parser.NumexprContext,0)


        def stringexpr(self):
            return self.getTypedRuleContext(MT22Parser.StringexprContext,0)


        def boolexpr(self):
            return self.getTypedRuleContext(MT22Parser.BoolexprContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Call_stmtContext,0)


        def access(self):
            return self.getTypedRuleContext(MT22Parser.AccessContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.numexpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.stringexpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.boolexpr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.call_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerexpr(self):
            return self.getTypedRuleContext(MT22Parser.IntegerexprContext,0)


        def floatexpr(self):
            return self.getTypedRuleContext(MT22Parser.FloatexprContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Call_stmtContext,0)


        def numexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.NumexprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.NumexprContext,i)


        def numop(self):
            return self.getTypedRuleContext(MT22Parser.NumopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_numexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumexpr" ):
                return visitor.visitNumexpr(self)
            else:
                return visitor.visitChildren(self)



    def numexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.NumexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_numexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 116
                self.integerexpr(0)
                pass

            elif la_ == 2:
                self.state = 117
                self.floatexpr(0)
                pass

            elif la_ == 3:
                self.state = 118
                self.call_stmt()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.NumexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_numexpr)
                    self.state = 121
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 122
                    self.numop()
                    self.state = 123
                    self.numexpr(5) 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprlist)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.expr()
                self.state = 131
                self.match(MT22Parser.COMMA)
                self.state = 132
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def accesslist(self):
            return self.getTypedRuleContext(MT22Parser.AccesslistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess" ):
                return visitor.visitAccess(self)
            else:
                return visitor.visitChildren(self)




    def access(self):

        localctx = MT22Parser.AccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MT22Parser.ID)
            self.state = 138
            self.match(MT22Parser.LSB)
            self.state = 139
            self.accesslist()
            self.state = 140
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccesslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerexpr(self):
            return self.getTypedRuleContext(MT22Parser.IntegerexprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def accesslist(self):
            return self.getTypedRuleContext(MT22Parser.AccesslistContext,0)


        def access(self):
            return self.getTypedRuleContext(MT22Parser.AccessContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_accesslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccesslist" ):
                return visitor.visitAccesslist(self)
            else:
                return visitor.visitChildren(self)




    def accesslist(self):

        localctx = MT22Parser.AccesslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_accesslist)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.integerexpr(0)
                self.state = 143
                self.match(MT22Parser.COMMA)
                self.state = 144
                self.accesslist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.access()
                self.state = 147
                self.match(MT22Parser.COMMA)
                self.state = 148
                self.accesslist()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(MT22Parser.ValueContext,0)


        def boolexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.BoolexprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.BoolexprContext,i)


        def LOGICNOT(self):
            return self.getToken(MT22Parser.LOGICNOT, 0)

        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def NOTEQ(self):
            return self.getToken(MT22Parser.NOTEQ, 0)

        def MORE_(self):
            return self.getToken(MT22Parser.MORE_, 0)

        def MOREOREQ(self):
            return self.getToken(MT22Parser.MOREOREQ, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def LESSOREQ(self):
            return self.getToken(MT22Parser.LESSOREQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_boolexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolexpr" ):
                return visitor.visitBoolexpr(self)
            else:
                return visitor.visitChildren(self)



    def boolexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.BoolexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_boolexpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.value()
            self._ctx.stop = self._input.LT(-1)
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.BoolexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolexpr)
                    self.state = 156
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 157
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.LOGICNOT) | (1 << MT22Parser.AND) | (1 << MT22Parser.OR) | (1 << MT22Parser.EQ) | (1 << MT22Parser.NOTEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LESSOREQ) | (1 << MT22Parser.MORE_) | (1 << MT22Parser.MOREOREQ))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 158
                    self.boolexpr(3) 
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MT22Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MT22Parser.FALSE, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def STRING_TYPE(self):
            return self.getToken(MT22Parser.STRING_TYPE, 0)

        def INT_TYPE(self):
            return self.getToken(MT22Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(MT22Parser.FLOAT_TYPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MT22Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.FALSE) | (1 << MT22Parser.TRUE) | (1 << MT22Parser.ID) | (1 << MT22Parser.INT_TYPE) | (1 << MT22Parser.FLOAT_TYPE) | (1 << MT22Parser.STRING_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(MT22Parser.INT_TYPE, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def integerexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.IntegerexprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.IntegerexprContext,i)


        def numop(self):
            return self.getTypedRuleContext(MT22Parser.NumopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_integerexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerexpr" ):
                return visitor.visitIntegerexpr(self)
            else:
                return visitor.visitChildren(self)



    def integerexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.IntegerexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_integerexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INT_TYPE]:
                self.state = 167
                self.match(MT22Parser.INT_TYPE)
                pass
            elif token in [MT22Parser.ID]:
                self.state = 168
                self.match(MT22Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.IntegerexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_integerexpr)
                    self.state = 171
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 172
                    self.numop()
                    self.state = 173
                    self.integerexpr(4) 
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FloatexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_TYPE(self):
            return self.getToken(MT22Parser.FLOAT_TYPE, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def floatexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.FloatexprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.FloatexprContext,i)


        def numop(self):
            return self.getTypedRuleContext(MT22Parser.NumopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_floatexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatexpr" ):
                return visitor.visitFloatexpr(self)
            else:
                return visitor.visitChildren(self)



    def floatexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.FloatexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_floatexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.FLOAT_TYPE]:
                self.state = 181
                self.match(MT22Parser.FLOAT_TYPE)
                pass
            elif token in [MT22Parser.ID]:
                self.state = 182
                self.match(MT22Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.FloatexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_floatexpr)
                    self.state = 185
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 186
                    self.numop()
                    self.state = 187
                    self.floatexpr(4) 
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StringexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_TYPE(self):
            return self.getToken(MT22Parser.STRING_TYPE, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def stringexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StringexprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StringexprContext,i)


        def DBLCOL(self):
            return self.getToken(MT22Parser.DBLCOL, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_stringexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringexpr" ):
                return visitor.visitStringexpr(self)
            else:
                return visitor.visitChildren(self)



    def stringexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.StringexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_stringexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.STRING_TYPE]:
                self.state = 195
                self.match(MT22Parser.STRING_TYPE)
                pass
            elif token in [MT22Parser.ID]:
                self.state = 196
                self.match(MT22Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.StringexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stringexpr)
                    self.state = 199
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 200
                    self.match(MT22Parser.DBLCOL)
                    self.state = 201
                    self.stringexpr(4) 
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MT22Parser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(MT22Parser.Type_Context,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = MT22Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.id_list()
            self.state = 210
            self.match(MT22Parser.COLON)
            self.state = 211
            self.type_()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.ASSIGN:
                self.state = 212
                self.match(MT22Parser.ASSIGN)
                self.state = 213
                self.exprlist()


            self.state = 216
            self.match(MT22Parser.SEMI)

            if self._ctx.getText().__contains__('='):
            	lst = self._ctx.getText().split('=')
            	idlist = lst[0]
            	exprlist = lst[1]
            	exprlist = exprlist[:-1]
            	exprlist = exprlist.split(',')
            	idlist = idlist.split(',')
            	if len(idlist) != len(exprlist):
            		err = self._ctx.getChild(-1).symbol
            		raise Exception('Error on line ' + str(err.line) + ' col ' + str(err.column)+': '+str(err.text))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def arraylist(self):
            return self.getTypedRuleContext(MT22Parser.ArraylistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_var_decl" ):
                return visitor.visitArray_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_var_decl(self):

        localctx = MT22Parser.Array_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.id_list()
            self.state = 220
            self.match(MT22Parser.COLON)
            self.state = 221
            self.match(MT22Parser.ARRAY)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.ASSIGN:
                self.state = 222
                self.match(MT22Parser.ASSIGN)
                self.state = 223
                self.arraylist()


            self.state = 226
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def type_(self):
            return self.getTypedRuleContext(MT22Parser.Type_Context,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def arraylist(self):
            return self.getTypedRuleContext(MT22Parser.ArraylistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraylist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylist" ):
                return visitor.visitArraylist(self)
            else:
                return visitor.visitChildren(self)




    def arraylist(self):

        localctx = MT22Parser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arraylist)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(MT22Parser.ARRAY)
                self.state = 229
                self.dimension()
                self.state = 230
                self.match(MT22Parser.OF)
                self.state = 231
                self.type_()
                self.state = 232
                self.match(MT22Parser.COMMA)
                self.state = 233
                self.arraylist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(MT22Parser.ARRAY)
                self.state = 236
                self.dimension()
                self.state = 237
                self.match(MT22Parser.OF)
                self.state = 238
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def intlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MT22Parser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MT22Parser.LSB)
            self.state = 243
            self.intlist()
            self.state = 244
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerexpr(self):
            return self.getTypedRuleContext(MT22Parser.IntegerexprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def intlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_intlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntlist" ):
                return visitor.visitIntlist(self)
            else:
                return visitor.visitChildren(self)




    def intlist(self):

        localctx = MT22Parser.IntlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_intlist)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.integerexpr(0)
                self.state = 247
                self.match(MT22Parser.COMMA)
                self.state = 248
                self.intlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.integerexpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MT22Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_id_list)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(MT22Parser.ID)
                self.state = 254
                self.match(MT22Parser.COMMA)
                self.state = 255
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MT22Parser.Type_Context,0)


        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_function_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_type" ):
                return visitor.visitFunction_type(self)
            else:
                return visitor.visitChildren(self)




    def function_type(self):

        localctx = MT22Parser.Function_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_function_type)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.type_()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.match(MT22Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(MT22Parser.Type_Context,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 263
                self.match(MT22Parser.INHERIT)


            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 266
                self.match(MT22Parser.OUT)


            self.state = 269
            self.match(MT22Parser.ID)
            self.state = 270
            self.match(MT22Parser.COLON)
            self.state = 271
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(MT22Parser.Param_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MT22Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_param_list)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.param()
                self.state = 274
                self.match(MT22Parser.COMMA)
                self.state = 275
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def function_type(self):
            return self.getTypedRuleContext(MT22Parser.Function_typeContext,0)


        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def body(self):
            return self.getTypedRuleContext(MT22Parser.BodyContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def param_list(self):
            return self.getTypedRuleContext(MT22Parser.Param_listContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_func_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = MT22Parser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MT22Parser.ID)
            self.state = 281
            self.match(MT22Parser.COLON)
            self.state = 282
            self.match(MT22Parser.FUNCTION)
            self.state = 283
            self.function_type()
            self.state = 284
            self.match(MT22Parser.LP)
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.ID]:
                self.state = 285
                self.param_list()
                pass
            elif token in [MT22Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 289
            self.match(MT22Parser.RP)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 290
                self.match(MT22Parser.INHERIT)
                self.state = 291
                self.match(MT22Parser.ID)


            self.state = 294
            self.match(MT22Parser.LCB)
            self.state = 295
            self.body()
            self.state = 296
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MT22Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_body)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MT22Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(MT22Parser.ID)
            self.state = 303
            self.match(MT22Parser.ASSIGN)
            self.state = 304
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MT22Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MT22Parser.RETURN)
            self.state = 307
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def argument(self):
            return self.getTypedRuleContext(MT22Parser.ArgumentContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MT22Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(MT22Parser.ID)
            self.state = 310
            self.match(MT22Parser.LP)
            self.state = 311
            self.argument()
            self.state = 312
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def argument(self):
            return self.getTypedRuleContext(MT22Parser.ArgumentContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = MT22Parser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_argument)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(MT22Parser.ID)
                self.state = 315
                self.match(MT22Parser.COMMA)
                self.state = 316
                self.argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.expr()
                self.state = 318
                self.match(MT22Parser.COMMA)
                self.state = 319
                self.argument()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.match(MT22Parser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def boolexpr(self):
            return self.getTypedRuleContext(MT22Parser.BoolexprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def if_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.If_bodyContext)
            else:
                return self.getTypedRuleContext(MT22Parser.If_bodyContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MT22Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MT22Parser.IF)
            self.state = 327
            self.match(MT22Parser.LP)
            self.state = 328
            self.boolexpr(0)
            self.state = 329
            self.match(MT22Parser.RP)

            self.state = 330
            self.if_body()
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 331
                self.match(MT22Parser.ELSE)
                self.state = 332
                self.if_body()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def integerexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.IntegerexprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.IntegerexprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def boolexpr(self):
            return self.getTypedRuleContext(MT22Parser.BoolexprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def loop_body(self):
            return self.getTypedRuleContext(MT22Parser.Loop_bodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MT22Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MT22Parser.FOR)
            self.state = 337
            self.match(MT22Parser.LP)
            self.state = 338
            self.match(MT22Parser.ID)
            self.state = 339
            self.match(MT22Parser.ASSIGN)
            self.state = 340
            self.integerexpr(0)
            self.state = 341
            self.match(MT22Parser.COMMA)
            self.state = 342
            self.boolexpr(0)
            self.state = 343
            self.match(MT22Parser.COMMA)
            self.state = 344
            self.integerexpr(0)
            self.state = 345
            self.match(MT22Parser.RP)
            self.state = 346
            self.loop_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def boolexpr(self):
            return self.getTypedRuleContext(MT22Parser.BoolexprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def loop_body(self):
            return self.getTypedRuleContext(MT22Parser.Loop_bodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = MT22Parser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(MT22Parser.WHILE)
            self.state = 349
            self.match(MT22Parser.LP)
            self.state = 350
            self.boolexpr(0)
            self.state = 351
            self.match(MT22Parser.RP)
            self.state = 352
            self.loop_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def loop_body(self):
            return self.getTypedRuleContext(MT22Parser.Loop_bodyContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def boolexpr(self):
            return self.getTypedRuleContext(MT22Parser.BoolexprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = MT22Parser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(MT22Parser.DO)
            self.state = 355
            self.loop_body()
            self.state = 356
            self.match(MT22Parser.WHILE)
            self.state = 357
            self.match(MT22Parser.LP)
            self.state = 358
            self.boolexpr(0)
            self.state = 359
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_if_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_body" ):
                return visitor.visitIf_body(self)
            else:
                return visitor.visitChildren(self)




    def if_body(self):

        localctx = MT22Parser.If_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_if_body)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(MT22Parser.LCB)
                self.state = 363
                self.stmtlist()
                self.state = 364
                self.match(MT22Parser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def loop(self):
            return self.getTypedRuleContext(MT22Parser.LoopContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_loop_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_body" ):
                return visitor.visitLoop_body(self)
            else:
                return visitor.visitChildren(self)




    def loop_body(self):

        localctx = MT22Parser.Loop_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_loop_body)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(MT22Parser.LCB)
                self.state = 370
                self.loop()
                self.state = 371
                self.match(MT22Parser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def loop(self):
            return self.getTypedRuleContext(MT22Parser.LoopContext,0)


        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = MT22Parser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_loop)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.LCB, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.stmt()
                self.state = 376
                self.loop()
                pass
            elif token in [MT22Parser.BREAK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.match(MT22Parser.BREAK)
                self.state = 379
                self.match(MT22Parser.SEMI)
                self.state = 380
                self.loop()
                pass
            elif token in [MT22Parser.CONTINUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.match(MT22Parser.CONTINUE)
                self.state = 382
                self.match(MT22Parser.SEMI)
                self.state = 383
                self.loop()
                pass
            elif token in [MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MT22Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(MT22Parser.LCB)
            self.state = 388
            self.stmtlist()
            self.state = 389
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDOP(self):
            return self.getToken(MT22Parser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def MULOP(self):
            return self.getToken(MT22Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MT22Parser.DIVOP, 0)

        def MODULO(self):
            return self.getToken(MT22Parser.MODULO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_numop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumop" ):
                return visitor.visitNumop(self)
            else:
                return visitor.visitChildren(self)




    def numop(self):

        localctx = MT22Parser.NumopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_numop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.ADDOP) | (1 << MT22Parser.SUBOP) | (1 << MT22Parser.MULOP) | (1 << MT22Parser.DIVOP) | (1 << MT22Parser.MODULO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.numexpr_sempred
        self._predicates[9] = self.boolexpr_sempred
        self._predicates[11] = self.integerexpr_sempred
        self._predicates[12] = self.floatexpr_sempred
        self._predicates[13] = self.stringexpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def numexpr_sempred(self, localctx:NumexprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

    def boolexpr_sempred(self, localctx:BoolexprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def integerexpr_sempred(self, localctx:IntegerexprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

    def floatexpr_sempred(self, localctx:FloatexprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

    def stringexpr_sempred(self, localctx:StringexprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




