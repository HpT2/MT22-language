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
        buf.write("\u01d4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\65\5\65\u015d\n\65\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\5\65\u0167\n\65\3\65\3\65\3\66\3\66\3\66\5\66")
        buf.write("\u016e\n\66\3\66\6\66\u0171\n\66\r\66\16\66\u0172\7\66")
        buf.write("\u0175\n\66\f\66\16\66\u0178\13\66\5\66\u017a\n\66\3\67")
        buf.write("\3\67\7\67\u017e\n\67\f\67\16\67\u0181\13\67\38\38\58")
        buf.write("\u0185\n8\38\68\u0188\n8\r8\168\u0189\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\39\39\39\79\u019d\n9\f9\169")
        buf.write("\u01a0\139\39\39\59\u01a4\n9\3:\3:\3:\3;\3;\3;\3<\3<\3")
        buf.write("<\3=\6=\u01b0\n=\r=\16=\u01b1\3=\3=\3>\3>\3>\3?\3?\7?")
        buf.write("\u01bb\n?\f?\16?\u01be\13?\3?\3?\3@\3@\7@\u01c4\n@\f@")
        buf.write("\16@\u01c7\13@\3@\5@\u01ca\n@\3@\7@\u01cd\n@\f@\16@\u01d0")
        buf.write("\13@\3@\3@\3@\4\u013d\u01c5\2A\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\2m\2o\2q\67s\2u\2w\2y8{9}:\177;")
        buf.write("\3\2\16\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63")
        buf.write(";\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$))\5\2\13\f\17\17\"")
        buf.write("\"\4\2\f\f$$\3\2$$\3\3\f\f\2\u01e8\2\3\3\2\2\2\2\5\3\2")
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
        buf.write("q\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\3\u0081\3\2\2\2\5\u0086\3\2\2\2\7\u008c\3\2\2\2\t\u0094")
        buf.write("\3\2\2\2\13\u0097\3\2\2\2\r\u009c\3\2\2\2\17\u00a2\3\2")
        buf.write("\2\2\21\u00a8\3\2\2\2\23\u00ac\3\2\2\2\25\u00b5\3\2\2")
        buf.write("\2\27\u00b8\3\2\2\2\31\u00c0\3\2\2\2\33\u00c7\3\2\2\2")
        buf.write("\35\u00ce\3\2\2\2\37\u00d3\3\2\2\2!\u00d9\3\2\2\2#\u00de")
        buf.write("\3\2\2\2%\u00e2\3\2\2\2\'\u00eb\3\2\2\2)\u00ee\3\2\2\2")
        buf.write("+\u00f6\3\2\2\2-\u00fc\3\2\2\2/\u00fe\3\2\2\2\61\u0100")
        buf.write("\3\2\2\2\63\u0102\3\2\2\2\65\u0104\3\2\2\2\67\u0106\3")
        buf.write("\2\2\29\u0108\3\2\2\2;\u010b\3\2\2\2=\u010e\3\2\2\2?\u0111")
        buf.write("\3\2\2\2A\u0114\3\2\2\2C\u0116\3\2\2\2E\u0119\3\2\2\2")
        buf.write("G\u011b\3\2\2\2I\u011e\3\2\2\2K\u0121\3\2\2\2M\u0123\3")
        buf.write("\2\2\2O\u0125\3\2\2\2Q\u0127\3\2\2\2S\u0129\3\2\2\2U\u012b")
        buf.write("\3\2\2\2W\u012d\3\2\2\2Y\u012f\3\2\2\2[\u0131\3\2\2\2")
        buf.write("]\u0133\3\2\2\2_\u0135\3\2\2\2a\u0137\3\2\2\2c\u0145\3")
        buf.write("\2\2\2e\u0150\3\2\2\2g\u0157\3\2\2\2i\u0166\3\2\2\2k\u0179")
        buf.write("\3\2\2\2m\u017b\3\2\2\2o\u0182\3\2\2\2q\u01a3\3\2\2\2")
        buf.write("s\u01a5\3\2\2\2u\u01a8\3\2\2\2w\u01ab\3\2\2\2y\u01af\3")
        buf.write("\2\2\2{\u01b5\3\2\2\2}\u01b8\3\2\2\2\177\u01c1\3\2\2\2")
        buf.write("\u0081\u0082\7c\2\2\u0082\u0083\7w\2\2\u0083\u0084\7v")
        buf.write("\2\2\u0084\u0085\7q\2\2\u0085\4\3\2\2\2\u0086\u0087\7")
        buf.write("d\2\2\u0087\u0088\7t\2\2\u0088\u0089\7g\2\2\u0089\u008a")
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
        buf.write("d\3\2\2\2\u0150\u0154\t\3\2\2\u0151\u0153\t\4\2\2\u0152")
        buf.write("\u0151\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2")
        buf.write("\u0154\u0155\3\2\2\2\u0155f\3\2\2\2\u0156\u0154\3\2\2")
        buf.write("\2\u0157\u0158\5k\66\2\u0158\u0159\b\64\3\2\u0159h\3\2")
        buf.write("\2\2\u015a\u015c\5k\66\2\u015b\u015d\5m\67\2\u015c\u015b")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u015f\5o8\2\u015f\u0167\3\2\2\2\u0160\u0161\5k\66\2\u0161")
        buf.write("\u0162\5m\67\2\u0162\u0167\3\2\2\2\u0163\u0164\5m\67\2")
        buf.write("\u0164\u0165\5o8\2\u0165\u0167\3\2\2\2\u0166\u015a\3\2")
        buf.write("\2\2\u0166\u0160\3\2\2\2\u0166\u0163\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168\u0169\b\65\4\2\u0169j\3\2\2\2\u016a\u017a")
        buf.write("\7\62\2\2\u016b\u0176\t\5\2\2\u016c\u016e\7a\2\2\u016d")
        buf.write("\u016c\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\3\2\2\2")
        buf.write("\u016f\u0171\t\6\2\2\u0170\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0175")
        buf.write("\3\2\2\2\u0174\u016d\3\2\2\2\u0175\u0178\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u017a\3\2\2\2")
        buf.write("\u0178\u0176\3\2\2\2\u0179\u016a\3\2\2\2\u0179\u016b\3")
        buf.write("\2\2\2\u017al\3\2\2\2\u017b\u017f\7\60\2\2\u017c\u017e")
        buf.write("\t\6\2\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180n\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0184\t\7\2\2\u0183\u0185\t\b\2\2")
        buf.write("\u0184\u0183\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\3")
        buf.write("\2\2\2\u0186\u0188\t\6\2\2\u0187\u0186\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("p\3\2\2\2\u018b\u018c\7$\2\2\u018c\u01a4\7$\2\2\u018d")
        buf.write("\u019e\7$\2\2\u018e\u019d\n\t\2\2\u018f\u0190\7^\2\2\u0190")
        buf.write("\u019d\7v\2\2\u0191\u0192\7^\2\2\u0192\u019d\7t\2\2\u0193")
        buf.write("\u0194\7^\2\2\u0194\u019d\7p\2\2\u0195\u0196\7^\2\2\u0196")
        buf.write("\u019d\7d\2\2\u0197\u0198\7^\2\2\u0198\u019d\7h\2\2\u0199")
        buf.write("\u019d\5s:\2\u019a\u019d\5u;\2\u019b\u019d\5w<\2\u019c")
        buf.write("\u018e\3\2\2\2\u019c\u018f\3\2\2\2\u019c\u0191\3\2\2\2")
        buf.write("\u019c\u0193\3\2\2\2\u019c\u0195\3\2\2\2\u019c\u0197\3")
        buf.write("\2\2\2\u019c\u0199\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019b")
        buf.write("\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a1\u01a2\7$\2\2\u01a2\u01a4\b9\5\2\u01a3\u018b\3\2")
        buf.write("\2\2\u01a3\u018d\3\2\2\2\u01a4r\3\2\2\2\u01a5\u01a6\7")
        buf.write("^\2\2\u01a6\u01a7\7)\2\2\u01a7t\3\2\2\2\u01a8\u01a9\7")
        buf.write("^\2\2\u01a9\u01aa\7$\2\2\u01aav\3\2\2\2\u01ab\u01ac\7")
        buf.write("^\2\2\u01ac\u01ad\7^\2\2\u01adx\3\2\2\2\u01ae\u01b0\t")
        buf.write("\n\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b4\b=\2\2\u01b4z\3\2\2\2\u01b5\u01b6\13\2\2\2\u01b6")
        buf.write("\u01b7\b>\6\2\u01b7|\3\2\2\2\u01b8\u01bc\7$\2\2\u01b9")
        buf.write("\u01bb\n\13\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01be\3\2\2")
        buf.write("\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bf")
        buf.write("\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0\b?\7\2\u01c0")
        buf.write("~\3\2\2\2\u01c1\u01c5\7$\2\2\u01c2\u01c4\n\f\2\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3")
        buf.write("\2\2\2\u01c8\u01ca\t\r\2\2\u01c9\u01c8\3\2\2\2\u01ca\u01ce")
        buf.write("\3\2\2\2\u01cb\u01cd\n\f\2\2\u01cc\u01cb\3\2\2\2\u01cd")
        buf.write("\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2\7")
        buf.write("$\2\2\u01d2\u01d3\b@\b\2\u01d3\u0080\3\2\2\2\27\2\u013d")
        buf.write("\u014b\u0154\u015c\u0166\u016d\u0172\u0176\u0179\u017f")
        buf.write("\u0184\u0189\u019c\u019e\u01a3\u01b1\u01bc\u01c5\u01c9")
        buf.write("\u01ce\t\b\2\2\3\64\2\3\65\3\39\4\3>\5\3?\6\3@\7")
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
     


