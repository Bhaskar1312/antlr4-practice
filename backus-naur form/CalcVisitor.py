# Generated from Calc.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#exprs.
    def visitExprs(self, ctx:CalcParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#expr.
    def visitExpr(self, ctx:CalcParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#sum.
    def visitSum(self, ctx:CalcParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#mul.
    def visitMul(self, ctx:CalcParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#last.
    def visitLast(self, ctx:CalcParser.LastContext):
        return self.visitChildren(ctx)



del CalcParser