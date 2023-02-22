grammar MT22;

@lexer::header {
#2012385
from lexererr import *
}

options{
	language=Python3;
}

program:  stmtlist  EOF ;

stmtlist			: stmt stmtlist | stmt | ;
stmt				: declaration | block_stmt | ( assignment | return_stmt | call_stmt | do_while_stmt ) SEMI 
					| if_stmt | for_stmt | while_stmt;

declaration			: var_declare | func_declare | array_var_decl ;

expr 				: numexpr1 | stringexpr | bool_res_expr1 | call_stmt | indexop;
bool_res_expr1		: boolexpr1 | bool_res_expr2 ;
bool_res_expr2		: relational_expr ; 
exprlist			: expr COMMA exprlist | expr ;

//num expression
numexpr1			: numexpr1 ADDOP numexpr2 | numexpr1 SUBOP numexpr2 | numexpr2; 
numexpr2			: numexpr2 MULOP numexpr3 | numexpr2 DIVOP numexpr3 | numexpr2 MODULO numexpr3 | numexpr3 ;
numexpr3			: sign_negation  | numexpr ;
numexpr 			: INT_TYPE | FLOAT_TYPE | call_stmt | ID |  LP numexpr1 RP ;

//Negation
sign_negation		: '-'(INT_TYPE | FLOAT_TYPE | LP numexpr1 RP);

indexop 			: ID LSB indexlist RSB ;
indexlist			: numexpr1 COMMA indexlist | indexop COMMA indexlist | indexop | numexpr1;

/*
indexed_array 		: LCB exprlist RCB ;
vallist				: val COMMA 
val					: INT_TYPE | FLOAT_TYPE | STRING_TYPE ;
*/

//Bool expression
boolexpr1 			: boolexpr1 AND boolexpr2 | boolexpr1 OR boolexpr2 | boolexpr2 ;
boolexpr2			: LOGICNOT boolexpr2 | boolval | relational_expr;

//Relational expression
relational_expr		: int_bool_rel | int_float_rel ;
int_bool_rel		: int_bool_rel EQ int_bool_rel | int_bool_rel NOTEQ int_bool_rel | boolval | INT_TYPE ;
int_float_rel		: int_float_rel (LESS | MORE_ | LESSOREQ | MOREOREQ ) int_float_rel | INT_TYPE | FLOAT_TYPE |ID ;

//Bool value
boolval				: TRUE | FALSE | LP boolexpr1 RP | ID | LP relational_expr RP ;

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
intlist			: numexpr1 COMMA intlist | numexpr1 ;
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
if_stmt			: IF LP boolexpr1 RP ( if_body ) ( ELSE if_body | );
for_stmt		: FOR LP ID ASSIGN numexpr1 COMMA boolexpr1 COMMA numexpr1 RP loop_body ;
while_stmt		: WHILE LP boolexpr1 RP loop_body  ;
do_while_stmt	: DO loop_body WHILE LP boolexpr1 RP;
if_body			: stmt | LCB stmtlist RCB ;
loop_body 		: stmt | LCB loop RCB ;
loop			: stmt loop | BREAK SEMI loop | CONTINUE SEMI loop | ;
block_stmt		: LCB stmtlist RCB ;


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



ID					: [A-Za-z_][A-Za-z0-9_]* ;
INT_TYPE			: INTPART {self.text = self.text.replace('_','')} ;
FLOAT_TYPE			: INTPART DECIMAL? EXPONENT? {self.text = self.text.replace('_','')} ;
fragment INTPART 	: '0' | [1-9] ('_'? [0-9]+)*  ;
fragment DECIMAL	: '.' [0-9]+ ;
fragment EXPONENT	: [eE] [-+]? [0-9]+ ;
STRING_TYPE			: '"' (~["\\'\n] | '\\t' | '\\r' | '\\n' | '\\b' | '\\f' | QUOTE | DBLQUOTE | BACKSLASH)* ~[\n]'"' {self.text=self.text[1:-1]};
fragment QUOTE 		: '\\''\u0027' ;
fragment DBLQUOTE 	: '\\''"' ;
fragment BACKSLASH 	: '\\''\\' ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .  {raise ErrorToken(self.text)} ;

UNCLOSE_STRING: '"' (~["\n])* {raise UncloseString(self.text)};	

ILLEGAL_ESCAPE		: '"'.*? ( '\n' | EOF ) .*? '"' {raise IllegalEscape(self.text)};