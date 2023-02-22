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
        buf.write("\u01cd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n\62\f\62\16\62\u014d\13\62\3\62\3\62\3\63\3\63\7\63")
        buf.write("\u0153\n\63\f\63\16\63\u0156\13\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\5\65\u015d\n\65\3\65\5\65\u0160\n\65\3\65\3\65\3")
        buf.write("\66\3\66\5\66\u0166\n\66\3\66\3\66\5\66\u016a\n\66\3\66")
        buf.write("\6\66\u016d\n\66\r\66\16\66\u016e\7\66\u0171\n\66\f\66")
        buf.write("\16\66\u0174\13\66\5\66\u0176\n\66\3\67\3\67\6\67\u017a")
        buf.write("\n\67\r\67\16\67\u017b\38\38\58\u0180\n8\38\68\u0183\n")
        buf.write("8\r8\168\u0184\39\39\39\39\39\39\39\39\39\39\39\39\39")
        buf.write("\39\39\79\u0196\n9\f9\169\u0199\139\39\39\39\39\3:\3:")
        buf.write("\3:\3;\3;\3;\3<\3<\3<\3=\6=\u01a9\n=\r=\16=\u01aa\3=\3")
        buf.write("=\3>\3>\3>\3?\3?\7?\u01b4\n?\f?\16?\u01b7\13?\3?\3?\3")
        buf.write("@\3@\7@\u01bd\n@\f@\16@\u01c0\13@\3@\5@\u01c3\n@\3@\7")
        buf.write("@\u01c6\n@\f@\16@\u01c9\13@\3@\3@\3@\5\u013d\u01be\u01c7")
        buf.write("\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2")
        buf.write("q\67s\2u\2w\2y8{9}:\177;\3\2\16\4\2\f\f\17\17\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\4\2--//\3\2\63;\3\2\62;\4\2GGgg\6\2")
        buf.write("\f\f$$))^^\3\2\f\f\5\2\13\f\17\17\"\"\4\2\f\f$$\3\3\f")
        buf.write("\f\2\u01e0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2q\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5\u0086")
        buf.write("\3\2\2\2\7\u008c\3\2\2\2\t\u0094\3\2\2\2\13\u0097\3\2")
        buf.write("\2\2\r\u009c\3\2\2\2\17\u00a2\3\2\2\2\21\u00a8\3\2\2\2")
        buf.write("\23\u00ac\3\2\2\2\25\u00b5\3\2\2\2\27\u00b8\3\2\2\2\31")
        buf.write("\u00c0\3\2\2\2\33\u00c7\3\2\2\2\35\u00ce\3\2\2\2\37\u00d3")
        buf.write("\3\2\2\2!\u00d9\3\2\2\2#\u00de\3\2\2\2%\u00e2\3\2\2\2")
        buf.write("\'\u00eb\3\2\2\2)\u00ee\3\2\2\2+\u00f6\3\2\2\2-\u00fc")
        buf.write("\3\2\2\2/\u00fe\3\2\2\2\61\u0100\3\2\2\2\63\u0102\3\2")
        buf.write("\2\2\65\u0104\3\2\2\2\67\u0106\3\2\2\29\u0108\3\2\2\2")
        buf.write(";\u010b\3\2\2\2=\u010e\3\2\2\2?\u0111\3\2\2\2A\u0114\3")
        buf.write("\2\2\2C\u0116\3\2\2\2E\u0119\3\2\2\2G\u011b\3\2\2\2I\u011e")
        buf.write("\3\2\2\2K\u0121\3\2\2\2M\u0123\3\2\2\2O\u0125\3\2\2\2")
        buf.write("Q\u0127\3\2\2\2S\u0129\3\2\2\2U\u012b\3\2\2\2W\u012d\3")
        buf.write("\2\2\2Y\u012f\3\2\2\2[\u0131\3\2\2\2]\u0133\3\2\2\2_\u0135")
        buf.write("\3\2\2\2a\u0137\3\2\2\2c\u0145\3\2\2\2e\u0150\3\2\2\2")
        buf.write("g\u0157\3\2\2\2i\u015a\3\2\2\2k\u0175\3\2\2\2m\u0177\3")
        buf.write("\2\2\2o\u017d\3\2\2\2q\u0186\3\2\2\2s\u019e\3\2\2\2u\u01a1")
        buf.write("\3\2\2\2w\u01a4\3\2\2\2y\u01a8\3\2\2\2{\u01ae\3\2\2\2")
        buf.write("}\u01b1\3\2\2\2\177\u01ba\3\2\2\2\u0081\u0082\7c\2\2\u0082")
        buf.write("\u0083\7w\2\2\u0083\u0084\7v\2\2\u0084\u0085\7q\2\2\u0085")
        buf.write("\4\3\2\2\2\u0086\u0087\7d\2\2\u0087\u0088\7t\2\2\u0088")
        buf.write("\u0089\7g\2\2\u0089\u008a\7c\2\2\u008a\u008b\7m\2\2\u008b")
        buf.write("\6\3\2\2\2\u008c\u008d\7d\2\2\u008d\u008e\7q\2\2\u008e")
        buf.write("\u008f\7q\2\2\u008f\u0090\7n\2\2\u0090\u0091\7g\2\2\u0091")
        buf.write("\u0092\7c\2\2\u0092\u0093\7p\2\2\u0093\b\3\2\2\2\u0094")
        buf.write("\u0095\7f\2\2\u0095\u0096\7q\2\2\u0096\n\3\2\2\2\u0097")
        buf.write("\u0098\7g\2\2\u0098\u0099\7n\2\2\u0099\u009a\7u\2\2\u009a")
        buf.write("\u009b\7g\2\2\u009b\f\3\2\2\2\u009c\u009d\7h\2\2\u009d")
        buf.write("\u009e\7c\2\2\u009e\u009f\7n\2\2\u009f\u00a0\7u\2\2\u00a0")
        buf.write("\u00a1\7g\2\2\u00a1\16\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3")
        buf.write("\u00a4\7n\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6\7c\2\2\u00a6")
        buf.write("\u00a7\7v\2\2\u00a7\20\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9")
        buf.write("\u00aa\7q\2\2\u00aa\u00ab\7t\2\2\u00ab\22\3\2\2\2\u00ac")
        buf.write("\u00ad\7h\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af\7p\2\2\u00af")
        buf.write("\u00b0\7e\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7k\2\2\u00b2")
        buf.write("\u00b3\7q\2\2\u00b3\u00b4\7p\2\2\u00b4\24\3\2\2\2\u00b5")
        buf.write("\u00b6\7k\2\2\u00b6\u00b7\7h\2\2\u00b7\26\3\2\2\2\u00b8")
        buf.write("\u00b9\7k\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7v\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\u00bd\7i\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\u00bf\7t\2\2\u00bf\30\3\2\2\2\u00c0\u00c1\7t\2\2\u00c1")
        buf.write("\u00c2\7g\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7w\2\2\u00c4")
        buf.write("\u00c5\7t\2\2\u00c5\u00c6\7p\2\2\u00c6\32\3\2\2\2\u00c7")
        buf.write("\u00c8\7u\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7t\2\2\u00ca")
        buf.write("\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7i\2\2\u00cd")
        buf.write("\34\3\2\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7t\2\2\u00d0")
        buf.write("\u00d1\7w\2\2\u00d1\u00d2\7g\2\2\u00d2\36\3\2\2\2\u00d3")
        buf.write("\u00d4\7y\2\2\u00d4\u00d5\7j\2\2\u00d5\u00d6\7k\2\2\u00d6")
        buf.write("\u00d7\7n\2\2\u00d7\u00d8\7g\2\2\u00d8 \3\2\2\2\u00d9")
        buf.write("\u00da\7x\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7k\2\2\u00dc")
        buf.write("\u00dd\7f\2\2\u00dd\"\3\2\2\2\u00de\u00df\7q\2\2\u00df")
        buf.write("\u00e0\7w\2\2\u00e0\u00e1\7v\2\2\u00e1$\3\2\2\2\u00e2")
        buf.write("\u00e3\7e\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7p\2\2\u00e5")
        buf.write("\u00e6\7v\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7p\2\2\u00e8")
        buf.write("\u00e9\7w\2\2\u00e9\u00ea\7g\2\2\u00ea&\3\2\2\2\u00eb")
        buf.write("\u00ec\7q\2\2\u00ec\u00ed\7h\2\2\u00ed(\3\2\2\2\u00ee")
        buf.write("\u00ef\7k\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7j\2\2\u00f1")
        buf.write("\u00f2\7g\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7k\2\2\u00f4")
        buf.write("\u00f5\7v\2\2\u00f5*\3\2\2\2\u00f6\u00f7\7c\2\2\u00f7")
        buf.write("\u00f8\7t\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7c\2\2\u00fa")
        buf.write("\u00fb\7{\2\2\u00fb,\3\2\2\2\u00fc\u00fd\7-\2\2\u00fd")
        buf.write(".\3\2\2\2\u00fe\u00ff\7/\2\2\u00ff\60\3\2\2\2\u0100\u0101")
        buf.write("\7,\2\2\u0101\62\3\2\2\2\u0102\u0103\7\61\2\2\u0103\64")
        buf.write("\3\2\2\2\u0104\u0105\7\'\2\2\u0105\66\3\2\2\2\u0106\u0107")
        buf.write("\7#\2\2\u01078\3\2\2\2\u0108\u0109\7(\2\2\u0109\u010a")
        buf.write("\7(\2\2\u010a:\3\2\2\2\u010b\u010c\7~\2\2\u010c\u010d")
        buf.write("\7~\2\2\u010d<\3\2\2\2\u010e\u010f\7?\2\2\u010f\u0110")
        buf.write("\7?\2\2\u0110>\3\2\2\2\u0111\u0112\7#\2\2\u0112\u0113")
        buf.write("\7?\2\2\u0113@\3\2\2\2\u0114\u0115\7>\2\2\u0115B\3\2\2")
        buf.write("\2\u0116\u0117\7>\2\2\u0117\u0118\7?\2\2\u0118D\3\2\2")
        buf.write("\2\u0119\u011a\7@\2\2\u011aF\3\2\2\2\u011b\u011c\7@\2")
        buf.write("\2\u011c\u011d\7?\2\2\u011dH\3\2\2\2\u011e\u011f\7<\2")
        buf.write("\2\u011f\u0120\7<\2\2\u0120J\3\2\2\2\u0121\u0122\7*\2")
        buf.write("\2\u0122L\3\2\2\2\u0123\u0124\7+\2\2\u0124N\3\2\2\2\u0125")
        buf.write("\u0126\7]\2\2\u0126P\3\2\2\2\u0127\u0128\7_\2\2\u0128")
        buf.write("R\3\2\2\2\u0129\u012a\7\60\2\2\u012aT\3\2\2\2\u012b\u012c")
        buf.write("\7.\2\2\u012cV\3\2\2\2\u012d\u012e\7=\2\2\u012eX\3\2\2")
        buf.write("\2\u012f\u0130\7<\2\2\u0130Z\3\2\2\2\u0131\u0132\7}\2")
        buf.write("\2\u0132\\\3\2\2\2\u0133\u0134\7\177\2\2\u0134^\3\2\2")
        buf.write("\2\u0135\u0136\7?\2\2\u0136`\3\2\2\2\u0137\u0138\7\61")
        buf.write("\2\2\u0138\u0139\7,\2\2\u0139\u013d\3\2\2\2\u013a\u013c")
        buf.write("\13\2\2\2\u013b\u013a\3\2\2\2\u013c\u013f\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u0140\3\2\2\2")
        buf.write("\u013f\u013d\3\2\2\2\u0140\u0141\7,\2\2\u0141\u0142\7")
        buf.write("\61\2\2\u0142\u0143\3\2\2\2\u0143\u0144\b\61\2\2\u0144")
        buf.write("b\3\2\2\2\u0145\u0146\7\61\2\2\u0146\u0147\7\61\2\2\u0147")
        buf.write("\u014b\3\2\2\2\u0148\u014a\n\2\2\2\u0149\u0148\3\2\2\2")
        buf.write("\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014c\u014e\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f")
        buf.write("\b\62\2\2\u014fd\3\2\2\2\u0150\u0154\t\3\2\2\u0151\u0153")
        buf.write("\t\4\2\2\u0152\u0151\3\2\2\2\u0153\u0156\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155f\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0157\u0158\5k\66\2\u0158\u0159\b\64\3")
        buf.write("\2\u0159h\3\2\2\2\u015a\u015c\5k\66\2\u015b\u015d\5m\67")
        buf.write("\2\u015c\u015b\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f")
        buf.write("\3\2\2\2\u015e\u0160\5o8\2\u015f\u015e\3\2\2\2\u015f\u0160")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\b\65\4\2\u0162")
        buf.write("j\3\2\2\2\u0163\u0176\7\62\2\2\u0164\u0166\t\5\2\2\u0165")
        buf.write("\u0164\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167\u0172\t\6\2\2\u0168\u016a\7a\2\2\u0169\u0168\3")
        buf.write("\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u016d")
        buf.write("\t\7\2\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0171\3\2\2\2")
        buf.write("\u0170\u0169\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3")
        buf.write("\2\2\2\u0172\u0173\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0175\u0163\3\2\2\2\u0175\u0165\3\2\2\2\u0176")
        buf.write("l\3\2\2\2\u0177\u0179\7\60\2\2\u0178\u017a\t\7\2\2\u0179")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017cn\3\2\2\2\u017d\u017f\t\b\2")
        buf.write("\2\u017e\u0180\t\5\2\2\u017f\u017e\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0183\t\7\2\2\u0182")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185p\3\2\2\2\u0186\u0197\7$\2\2")
        buf.write("\u0187\u0196\n\t\2\2\u0188\u0189\7^\2\2\u0189\u0196\7")
        buf.write("v\2\2\u018a\u018b\7^\2\2\u018b\u0196\7t\2\2\u018c\u018d")
        buf.write("\7^\2\2\u018d\u0196\7p\2\2\u018e\u018f\7^\2\2\u018f\u0196")
        buf.write("\7d\2\2\u0190\u0191\7^\2\2\u0191\u0196\7h\2\2\u0192\u0196")
        buf.write("\5s:\2\u0193\u0196\5u;\2\u0194\u0196\5w<\2\u0195\u0187")
        buf.write("\3\2\2\2\u0195\u0188\3\2\2\2\u0195\u018a\3\2\2\2\u0195")
        buf.write("\u018c\3\2\2\2\u0195\u018e\3\2\2\2\u0195\u0190\3\2\2\2")
        buf.write("\u0195\u0192\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194\3")
        buf.write("\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198\u019a\3\2\2\2\u0199\u0197\3\2\2\2\u019a")
        buf.write("\u019b\n\n\2\2\u019b\u019c\7$\2\2\u019c\u019d\b9\5\2\u019d")
        buf.write("r\3\2\2\2\u019e\u019f\7^\2\2\u019f\u01a0\7)\2\2\u01a0")
        buf.write("t\3\2\2\2\u01a1\u01a2\7^\2\2\u01a2\u01a3\7$\2\2\u01a3")
        buf.write("v\3\2\2\2\u01a4\u01a5\7^\2\2\u01a5\u01a6\7^\2\2\u01a6")
        buf.write("x\3\2\2\2\u01a7\u01a9\t\13\2\2\u01a8\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01ac\u01ad\b=\2\2\u01adz\3\2\2\2")
        buf.write("\u01ae\u01af\13\2\2\2\u01af\u01b0\b>\6\2\u01b0|\3\2\2")
        buf.write("\2\u01b1\u01b5\7$\2\2\u01b2\u01b4\n\f\2\2\u01b3\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3\2\2\2")
        buf.write("\u01b8\u01b9\b?\7\2\u01b9~\3\2\2\2\u01ba\u01be\7$\2\2")
        buf.write("\u01bb\u01bd\13\2\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c3\t\r\2\2")
        buf.write("\u01c2\u01c1\3\2\2\2\u01c3\u01c7\3\2\2\2\u01c4\u01c6\13")
        buf.write("\2\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01ca\u01cb\7$\2\2\u01cb\u01cc\b@\b\2\u01cc")
        buf.write("\u0080\3\2\2\2\27\2\u013d\u014b\u0154\u015c\u015f\u0165")
        buf.write("\u0169\u016e\u0172\u0175\u017b\u017f\u0184\u0195\u0197")
        buf.write("\u01aa\u01b5\u01be\u01c2\u01c7\t\b\2\2\3\64\2\3\65\3\3")
        buf.write("9\4\3>\5\3?\6\3@\7")
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
    STRING_TYPE = 53
    WS = 54
    ERROR_CHAR = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57

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
            "ID", "INT_TYPE", "FLOAT_TYPE", "STRING_TYPE", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
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
            actions[50] = self.INT_TYPE_action 
            actions[51] = self.FLOAT_TYPE_action 
            actions[55] = self.STRING_TYPE_action 
            actions[60] = self.ERROR_CHAR_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
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
     


