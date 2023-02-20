grammar MT22;

@lexer::header {
#2012385
from lexererr import *
}

options{
	language=Python3;
}

program:  stmtlist  EOF ;

stmtlist		: stmt stmtlist | stmt ;
stmt			: declaration | ( assignment | return_stmt | call_stmt ) SEMI | if_stmt | for_stmt | while_stmt;

declaration		: var_declare | func_declare | array_var_decl ;

expr 			: numexpr | stringexpr | boolexpr | call_stmt;
numexpr			: numexpr numop numexpr | integerexpr | floatexpr | call_stmt;
exprlist		: expr COMMA exprlist | expr ;



access 	: ID LSB intlist RSB ;

/*
indexed_array 	: LCB exprlist RCB ;
vallist			: val COMMA 
val				: INT_TYPE | FLOAT_TYPE | STRING_TYPE ;
*/

//Bool expr
boolexpr 	: boolexpr ( LOGICNOT | AND | OR | EQ | NOTEQ ) boolexpr | value;
value		: TRUE | FALSE | ID | STRING_TYPE | INT_TYPE | FLOAT_TYPE ;

//Integer expr
integerexpr	: integerexpr numop integerexpr | INT_TYPE | ID ;

//Float expr
floatexpr 	: floatexpr numop floatexpr | FLOAT_TYPE | ID ;

//String expr
stringexpr	: stringexpr DBLCOL stringexpr | STRING_TYPE | ID ;

//Type
type_	: INTEGER | FLOAT | STRING | BOOLEAN ;

//Var declaration
var_declare	: id_list COLON type_ ( ASSIGN exprlist )? SEMI 
{
if self._ctx.getText().__contains__('='):
	lst = self._ctx.getText().split('=')
	idlist = lst[0]
	exprlist = lst[1]
	exprlist = exprlist[:-1]
	exprlist = exprlist.split(',')
	idlist = idlist.split(',')
	if len(idlist) != len(exprlist):
		err = self._ctx.getChild(-1).symbol
		raise Exception('Error on line ' + str(err.line) + ' col ' + str(err.column)+': '+str(err.text))
};
array_var_decl	: id_list COLON ARRAY (ASSIGN arraylist)? SEMI ;
arraylist		: ARRAY dimension OF type_ COMMA arraylist | ARRAY dimension OF type_;
dimension		: LSB intlist RSB ;
intlist			: INT_TYPE COMMA intlist | INT_TYPE ;
id_list			: ID COMMA id_list | ID ;


//function declarations
function_type	: type_ | VOID ;
param			: INHERIT? OUT? ID COLON type_ ;
param_list		: param COMMA param_list | param ;
func_declare	: ID COLON FUNCTION function_type LP ( param_list | ) RP (INHERIT ID)? LCB body RCB;
body			: stmtlist |  ;

assignment		: ID ASSIGN expr;
return_stmt		: RETURN expr ;
call_stmt		: ID LP argument RP ;
argument		: ID COMMA argument | expr COMMA argument | ID | expr | ;
if_stmt			: IF LP boolexpr RP ( loop_if_body ) ( ELSE loop_if_body | );
for_stmt		: 'for_stmt' ;
while_stmt		: 'while_stmt' ;
loop_if_body	: stmt | LCB stmtlist RCB ;

//Num Operators
numop		: ADDOP | SUBOP | MULOP | DIVOP | MODULO | EQ | NOTEQ | MORE_ | MOREOREQ | LESS | LESSOREQ  ;

//Keywords
AUTO		: 'auto'  ;
BREAK		: 'break' ;
BOOLEAN		: 'boolean' ;
DO			: 'do' ;
ELSE		: 'else' ;
FALSE		: 'false' ;
FLOAT		: 'float' ;
FOR 		: 'for' ;
FUNCTION	: 'function' ;
IF			: 'if' ;
INTEGER		: 'integer' ;
RETURN 		: 'return' ;
STRING 		: 'string' ;
TRUE		: 'true' ;
WHILE		: 'while' ;
VOID 		: 'void' ;
OUT			: 'out' ;
CONTINUE	: 'continue' ;
OF 			: 'of' ;
INHERIT		: 'inherit' ;
ARRAY		: 'array' ;

//Operators
ADDOP		: '+' ;
SUBOP		: '-' ;
MULOP		: '*' ;
DIVOP		: '/' ;
MODULO		: '%' ;
LOGICNOT	: '!' ;
AND			: '&&';
OR 			: '||';
EQ			: '==';
NOTEQ		: '!=';
LESS		: '<' ;
LESSOREQ	: '<=';
MORE_		: '>' ;
MOREOREQ	: '>=';
DBLCOL		: '::';

//Seperators
LP			: '(' ;
RP			: ')' ;
LSB			: '[' ;
RSB			: ']' ;
DOT			: '.' ;
COMMA		: ',' ;
SEMI		: ';' ;
COLON		: ':' ;
LCB			: '{' ;
RCB			: '}' ;
ASSIGN		: '=' ;


COMMENT 	: '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//'  (~[\r\n])* -> skip	;

ILLEGAL_ESCAPE		: ('"' ('\\n' | EOF ) .*?  '"'
					| '"' .*? ('\\n' | EOF) '"'
					| '"' ('\\n' | EOF) .*? ('\\n' | EOF) ) {raise IllegalEscape(self.text)};

ID					: [A-Za-z_][A-Za-z0-9_]* ;
INT_TYPE			: INTPART {self.text = self.text.replace('_','')} ;
FLOAT_TYPE			: INTPART DECIMAL? EXPONENT? {self.text = self.text.replace('_','')} ;
fragment INTPART 	: '0' | [+-]? [1-9] ('_'? [0-9]+)*  ;
fragment DECIMAL	: '.' [0-9]+ ;
fragment EXPONENT	: [eE] [-+]? [0-9]+ ;
STRING_TYPE			: '"' (~["\\'] | '\\t' | '\\r' | '\\n' | '\\b' | '\\f' | QUOTE | DBLQUOTE | BACKSLASH)* '"' {self.text=self.text[1:-1]};
fragment QUOTE 		: '\\''\u0027' ;
fragment DBLQUOTE 	: '\\''"' ;
fragment BACKSLASH 	: '\\''\\' ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .  {raise ErrorToken(self.text)} ;
UNCLOSE_STRING: '"' (~["])* {raise UncloseString(self.text)};

