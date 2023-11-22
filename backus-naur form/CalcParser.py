# Generated from Calc.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        28,8,2,10,2,12,2,31,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,39,8,3,1,3,1,
        3,1,3,5,3,44,8,3,10,3,12,3,47,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,56,8,4,1,4,0,2,4,6,5,0,2,4,6,8,0,2,1,0,2,3,1,0,4,5,58,0,13,1,0,
        0,0,2,18,1,0,0,0,4,21,1,0,0,0,6,38,1,0,0,0,8,55,1,0,0,0,10,12,3,
        2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,
        16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,3,4,2,
        0,19,20,5,1,0,0,20,3,1,0,0,0,21,22,6,2,-1,0,22,23,3,6,3,0,23,29,
        1,0,0,0,24,25,10,1,0,0,25,26,7,0,0,0,26,28,3,6,3,0,27,24,1,0,0,0,
        28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,5,1,0,0,0,31,29,1,0,
        0,0,32,33,6,3,-1,0,33,39,3,8,4,0,34,35,5,6,0,0,35,36,3,6,3,0,36,
        37,5,7,0,0,37,39,1,0,0,0,38,32,1,0,0,0,38,34,1,0,0,0,39,45,1,0,0,
        0,40,41,10,2,0,0,41,42,7,1,0,0,42,44,3,8,4,0,43,40,1,0,0,0,44,47,
        1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,7,1,0,0,0,47,45,1,0,0,0,48,
        56,5,8,0,0,49,50,7,0,0,0,50,56,3,8,4,0,51,52,5,6,0,0,52,53,3,4,2,
        0,53,54,5,7,0,0,54,56,1,0,0,0,55,48,1,0,0,0,55,49,1,0,0,0,55,51,
        1,0,0,0,56,9,1,0,0,0,5,13,29,38,45,55
    ]

class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\r\\n'", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "SPACE" ]

    RULE_exprs = 0
    RULE_expr = 1
    RULE_sum = 2
    RULE_mul = 3
    RULE_last = 4

    ruleNames =  [ "exprs", "expr", "sum", "mul", "last" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUMBER=8
    SPACE=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalcParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_exprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprs" ):
                listener.enterExprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprs" ):
                listener.exitExprs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = CalcParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_exprs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 332) != 0:
                self.state = 10
                self.expr()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(CalcParser.EOF)
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

        def sum_(self):
            return self.getTypedRuleContext(CalcParser.SumContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CalcParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.sum_(0)
            self.state = 19
            self.match(CalcParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def mul(self):
            return self.getTypedRuleContext(CalcParser.MulContext,0)


        def sum_(self):
            return self.getTypedRuleContext(CalcParser.SumContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_sum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)



    def sum_(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.SumContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_sum, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.mul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CalcParser.SumContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_sum)
                    self.state = 24
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 25
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 26
                    self.mul(0) 
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def last(self):
            return self.getTypedRuleContext(CalcParser.LastContext,0)


        def mul(self):
            return self.getTypedRuleContext(CalcParser.MulContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)



    def mul(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.MulContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_mul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 33
                self.last()
                pass

            elif la_ == 2:
                self.state = 34
                self.match(CalcParser.T__5)
                self.state = 35
                self.mul(0)
                self.state = 36
                self.match(CalcParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CalcParser.MulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul)
                    self.state = 40
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 41
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==4 or _la==5):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 42
                    self.last() 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LastContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.num = None # Token
            self.op = None # Token

        def NUMBER(self):
            return self.getToken(CalcParser.NUMBER, 0)

        def last(self):
            return self.getTypedRuleContext(CalcParser.LastContext,0)


        def sum_(self):
            return self.getTypedRuleContext(CalcParser.SumContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_last

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLast" ):
                listener.enterLast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLast" ):
                listener.exitLast(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLast" ):
                return visitor.visitLast(self)
            else:
                return visitor.visitChildren(self)




    def last(self):

        localctx = CalcParser.LastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_last)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                localctx.num = self.match(CalcParser.NUMBER)
                pass
            elif token in [2, 3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 50
                self.last()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(CalcParser.T__5)
                self.state = 52
                self.sum_(0)
                self.state = 53
                self.match(CalcParser.T__6)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.sum_sempred
        self._predicates[3] = self.mul_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def sum_sempred(self, localctx:SumContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def mul_sempred(self, localctx:MulContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




