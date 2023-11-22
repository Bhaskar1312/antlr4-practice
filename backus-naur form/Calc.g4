grammar Calc;

// <expr> ::= <sum>
// <sum> ::= <mul> | <sum> "+" <mul> | <sum> "-" <mul>
// <mul> ::= <last> | <mul> "*" <last> | <mul> "/" <last>
// <last> ::= <number> | "+" <last> | "-" <last> | "(" <expr> ")"
// <number> ::= <digit> | <digit> <number>
// <digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" 

// Lexer rules
NUMBER: [0-9]+;
SPACE: (' ' | '\t') -> skip;

// Parser rules
exprs: expr* EOF;
expr: sum '\r\n';
sum: mul | sum op=('+' | '-') mul;
mul: last | mul op=('*' | '/') last;
last: num=NUMBER | op=('+' | '-') last | '(' sum ')';

// build: antlr4 Calc.g4 -Dlanguage=Python3 -visitor
// clean: rm -r .antlr;rm -r __pycache__ ; rm *.tokens *.interp CalcParser.py CalcVisitor.py CalcLexer.py

// parse: antlr4-parse Calc.g4 exprs -tree; antlr4-parse Calc.g4 exprs -gui