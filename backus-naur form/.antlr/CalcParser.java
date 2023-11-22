// Generated from c:/Users/Bhaskar/Downloads/Code/antlr/backus-naur form/Calc.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CalcParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, NUMBER=8, SPACE=9;
	public static final int
		RULE_exprs = 0, RULE_expr = 1, RULE_sum = 2, RULE_mul = 3, RULE_last = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"exprs", "expr", "sum", "mul", "last"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\r\\n'", "'+'", "'-'", "'*'", "'/'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "NUMBER", "SPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Calc.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CalcParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprsContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CalcParser.EOF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprs; }
	}

	public final ExprsContext exprs() throws RecognitionException {
		ExprsContext _localctx = new ExprsContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_exprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 332L) != 0)) {
				{
				{
				setState(10);
				expr();
				}
				}
				setState(15);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(16);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public SumContext sum() {
			return getRuleContext(SumContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			sum(0);
			setState(19);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SumContext extends ParserRuleContext {
		public Token op;
		public MulContext mul() {
			return getRuleContext(MulContext.class,0);
		}
		public SumContext sum() {
			return getRuleContext(SumContext.class,0);
		}
		public SumContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sum; }
	}

	public final SumContext sum() throws RecognitionException {
		return sum(0);
	}

	private SumContext sum(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		SumContext _localctx = new SumContext(_ctx, _parentState);
		SumContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_sum, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(22);
			mul(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(29);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new SumContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_sum);
					setState(24);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(25);
					((SumContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__1 || _la==T__2) ) {
						((SumContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(26);
					mul(0);
					}
					} 
				}
				setState(31);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MulContext extends ParserRuleContext {
		public Token op;
		public LastContext last() {
			return getRuleContext(LastContext.class,0);
		}
		public MulContext mul() {
			return getRuleContext(MulContext.class,0);
		}
		public MulContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mul; }
	}

	public final MulContext mul() throws RecognitionException {
		return mul(0);
	}

	private MulContext mul(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MulContext _localctx = new MulContext(_ctx, _parentState);
		MulContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_mul, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(33);
				last();
				}
				break;
			case 2:
				{
				setState(34);
				match(T__5);
				setState(35);
				mul(0);
				setState(36);
				match(T__6);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(45);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new MulContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_mul);
					setState(40);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(41);
					((MulContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__3 || _la==T__4) ) {
						((MulContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(42);
					last();
					}
					} 
				}
				setState(47);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LastContext extends ParserRuleContext {
		public Token num;
		public Token op;
		public TerminalNode NUMBER() { return getToken(CalcParser.NUMBER, 0); }
		public LastContext last() {
			return getRuleContext(LastContext.class,0);
		}
		public SumContext sum() {
			return getRuleContext(SumContext.class,0);
		}
		public LastContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_last; }
	}

	public final LastContext last() throws RecognitionException {
		LastContext _localctx = new LastContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_last);
		int _la;
		try {
			setState(55);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				((LastContext)_localctx).num = match(NUMBER);
				}
				break;
			case T__1:
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				((LastContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==T__1 || _la==T__2) ) {
					((LastContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(50);
				last();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 3);
				{
				setState(51);
				match(T__5);
				setState(52);
				sum(0);
				setState(53);
				match(T__6);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return sum_sempred((SumContext)_localctx, predIndex);
		case 3:
			return mul_sempred((MulContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean sum_sempred(SumContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean mul_sempred(MulContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\t:\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0005\u0000\f\b\u0000\n\u0000\f\u0000\u000f\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002\u001c\b\u0002"+
		"\n\u0002\f\u0002\u001f\t\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0003\u0003\'\b\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0005\u0003,\b\u0003\n\u0003\f\u0003/\t\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0003\u00048\b\u0004\u0001\u0004\u0000\u0002\u0004\u0006\u0005"+
		"\u0000\u0002\u0004\u0006\b\u0000\u0002\u0001\u0000\u0002\u0003\u0001\u0000"+
		"\u0004\u0005:\u0000\r\u0001\u0000\u0000\u0000\u0002\u0012\u0001\u0000"+
		"\u0000\u0000\u0004\u0015\u0001\u0000\u0000\u0000\u0006&\u0001\u0000\u0000"+
		"\u0000\b7\u0001\u0000\u0000\u0000\n\f\u0003\u0002\u0001\u0000\u000b\n"+
		"\u0001\u0000\u0000\u0000\f\u000f\u0001\u0000\u0000\u0000\r\u000b\u0001"+
		"\u0000\u0000\u0000\r\u000e\u0001\u0000\u0000\u0000\u000e\u0010\u0001\u0000"+
		"\u0000\u0000\u000f\r\u0001\u0000\u0000\u0000\u0010\u0011\u0005\u0000\u0000"+
		"\u0001\u0011\u0001\u0001\u0000\u0000\u0000\u0012\u0013\u0003\u0004\u0002"+
		"\u0000\u0013\u0014\u0005\u0001\u0000\u0000\u0014\u0003\u0001\u0000\u0000"+
		"\u0000\u0015\u0016\u0006\u0002\uffff\uffff\u0000\u0016\u0017\u0003\u0006"+
		"\u0003\u0000\u0017\u001d\u0001\u0000\u0000\u0000\u0018\u0019\n\u0001\u0000"+
		"\u0000\u0019\u001a\u0007\u0000\u0000\u0000\u001a\u001c\u0003\u0006\u0003"+
		"\u0000\u001b\u0018\u0001\u0000\u0000\u0000\u001c\u001f\u0001\u0000\u0000"+
		"\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000"+
		"\u0000\u001e\u0005\u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000\u0000"+
		"\u0000 !\u0006\u0003\uffff\uffff\u0000!\'\u0003\b\u0004\u0000\"#\u0005"+
		"\u0006\u0000\u0000#$\u0003\u0006\u0003\u0000$%\u0005\u0007\u0000\u0000"+
		"%\'\u0001\u0000\u0000\u0000& \u0001\u0000\u0000\u0000&\"\u0001\u0000\u0000"+
		"\u0000\'-\u0001\u0000\u0000\u0000()\n\u0002\u0000\u0000)*\u0007\u0001"+
		"\u0000\u0000*,\u0003\b\u0004\u0000+(\u0001\u0000\u0000\u0000,/\u0001\u0000"+
		"\u0000\u0000-+\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000.\u0007"+
		"\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000\u000008\u0005\b\u0000\u0000"+
		"12\u0007\u0000\u0000\u000028\u0003\b\u0004\u000034\u0005\u0006\u0000\u0000"+
		"45\u0003\u0004\u0002\u000056\u0005\u0007\u0000\u000068\u0001\u0000\u0000"+
		"\u000070\u0001\u0000\u0000\u000071\u0001\u0000\u0000\u000073\u0001\u0000"+
		"\u0000\u00008\t\u0001\u0000\u0000\u0000\u0005\r\u001d&-7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}