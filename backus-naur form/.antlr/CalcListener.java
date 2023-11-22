// Generated from c:/Users/Bhaskar/Downloads/Code/antlr/backus-naur form/Calc.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CalcParser}.
 */
public interface CalcListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CalcParser#exprs}.
	 * @param ctx the parse tree
	 */
	void enterExprs(CalcParser.ExprsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalcParser#exprs}.
	 * @param ctx the parse tree
	 */
	void exitExprs(CalcParser.ExprsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalcParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(CalcParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalcParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(CalcParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalcParser#sum}.
	 * @param ctx the parse tree
	 */
	void enterSum(CalcParser.SumContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalcParser#sum}.
	 * @param ctx the parse tree
	 */
	void exitSum(CalcParser.SumContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalcParser#mul}.
	 * @param ctx the parse tree
	 */
	void enterMul(CalcParser.MulContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalcParser#mul}.
	 * @param ctx the parse tree
	 */
	void exitMul(CalcParser.MulContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalcParser#last}.
	 * @param ctx the parse tree
	 */
	void enterLast(CalcParser.LastContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalcParser#last}.
	 * @param ctx the parse tree
	 */
	void exitLast(CalcParser.LastContext ctx);
}