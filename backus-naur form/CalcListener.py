# Generated from Calc.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#exprs.
    def enterExprs(self, ctx:CalcParser.ExprsContext):
        pass

    # Exit a parse tree produced by CalcParser#exprs.
    def exitExprs(self, ctx:CalcParser.ExprsContext):
        pass


    # Enter a parse tree produced by CalcParser#expr.
    def enterExpr(self, ctx:CalcParser.ExprContext):
        pass

    # Exit a parse tree produced by CalcParser#expr.
    def exitExpr(self, ctx:CalcParser.ExprContext):
        pass


    # Enter a parse tree produced by CalcParser#sum.
    def enterSum(self, ctx:CalcParser.SumContext):
        pass

    # Exit a parse tree produced by CalcParser#sum.
    def exitSum(self, ctx:CalcParser.SumContext):
        pass


    # Enter a parse tree produced by CalcParser#mul.
    def enterMul(self, ctx:CalcParser.MulContext):
        pass

    # Exit a parse tree produced by CalcParser#mul.
    def exitMul(self, ctx:CalcParser.MulContext):
        pass


    # Enter a parse tree produced by CalcParser#last.
    def enterLast(self, ctx:CalcParser.LastContext):
        pass

    # Exit a parse tree produced by CalcParser#last.
    def exitLast(self, ctx:CalcParser.LastContext):
        pass



del CalcParser