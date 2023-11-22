# Generated from Calc.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,43,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,
        4,1,5,1,5,1,6,1,6,1,7,4,7,36,8,7,11,7,12,7,37,1,8,1,8,1,8,1,8,0,
        0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,2,1,0,48,57,2,0,
        9,9,32,32,43,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,
        1,0,0,0,3,22,1,0,0,0,5,24,1,0,0,0,7,26,1,0,0,0,9,28,1,0,0,0,11,30,
        1,0,0,0,13,32,1,0,0,0,15,35,1,0,0,0,17,39,1,0,0,0,19,20,5,13,0,0,
        20,21,5,10,0,0,21,2,1,0,0,0,22,23,5,43,0,0,23,4,1,0,0,0,24,25,5,
        45,0,0,25,6,1,0,0,0,26,27,5,42,0,0,27,8,1,0,0,0,28,29,5,47,0,0,29,
        10,1,0,0,0,30,31,5,40,0,0,31,12,1,0,0,0,32,33,5,41,0,0,33,14,1,0,
        0,0,34,36,7,0,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,16,1,0,0,0,39,40,7,1,0,0,40,41,1,0,0,0,41,42,6,8,0,0,
        42,18,1,0,0,0,2,0,37,1,6,0,0
    ]

class CalcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    NUMBER = 8
    SPACE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\r\\n'", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "NUMBER", "SPACE" ]

    grammarFileName = "Calc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


