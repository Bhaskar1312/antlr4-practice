from antlr4 import FileStream, CommonTokenStream
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcVisitor import CalcVisitor


class Visitor(CalcVisitor):
    def visitExprs(self, ctx):
        for item in ctx.expr():
            print(self.visit(item))

    def visitExpr(self, ctx):
        return self.visit(ctx.sum_())

    def visitSum(self, ctx):
        if not ctx.op:
            return self.visit(ctx.mul())
        left = self.visit(ctx.sum_())
        right = self.visit(ctx.mul())
        if ctx.op.text == '+':
            return left + right
        elif ctx.op.text == '-':
            return left - right
        assert False

    def visitMul(self, ctx):
        if not ctx.op:
            return self.visit(ctx.last())
        left = self.visit(ctx.mul())
        right = self.visit(ctx.last())
        if ctx.op.text == '*':
            return left * right
        if ctx.op.text == '/':
            return left / right
        assert False

    def visitLast(self, ctx):
        if ctx.num:
            return float(ctx.num.text)
        if not ctx.op:
            return self.visit(ctx.sum())
        if ctx.op.text == '+':
            return self.visit(ctx.last())
        if ctx.op.text == '-':
            return -self.visit(ctx.last())
        assert False


in_stream = FileStream('test.txt')
lexer = CalcLexer(in_stream)
stream = CommonTokenStream(lexer) # stream of tokens
parser = CalcParser(stream)
tree = parser.exprs()
visitor = Visitor()
visitor.visit(tree)
