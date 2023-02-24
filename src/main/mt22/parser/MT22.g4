grammar MT22;
//Sửa thứ tự expr theo đề 
@lexer::header {
#2012385
from lexererr import *
}

options{
	language=Python3;
}

program:  prog EOF ;

prog				: stmtlist prog | declaration prog | stmtlist | declaration ;

stmtlist			: stmt stmtlist | stmt  ;
stmt				: block_stmt | var_declare
					| ( assignment | return_stmt | call_stmt | do_while_stmt | BREAK | CONTINUE ) SEMI 
					| if_stmt | for_stmt | while_stmt;

declaration			: var_declare | func_declare ;

expr 				: expr DBLCOL expr | expr1 ;
expr1				: expr1 (EQ | NOTEQ | LESS | MORE_ | LESSOREQ | MOREOREQ) expr1 | expr2 ;
expr2				: expr2 (OR | AND) expr3 | expr3 ;
expr3				: expr3 (ADDOP | SUBOP) expr4 | expr4 ;
expr4				: expr4 (MULOP | DIVOP | MODULO) expr5 | expr5 ;
expr5				: LOGICNOT expr5 | expr6 ;
expr6 				: '-'expr6 | expr7 ;
expr7 				: indexop | exprval;
exprval				: ID | INT_TYPE | FLOAT_TYPE | STRING_TYPE | indexlist | TRUE | FALSE | call_stmt
					| LP expr1 RP ;
exprlist			: expr COMMA exprlist | expr ;

//num int expression
numexpr1			: numexpr1 ADDOP numexpr2 | numexpr1 SUBOP numexpr2 | numexpr2; 
numexpr2			: numexpr2 MULOP numexpr3 | numexpr2 DIVOP numexpr3 | numexpr2 MODULO numexpr3 | numexpr3 ;
numexpr3			: '-'numexpr | numexpr | indexop ;
numexpr 			: INT_TYPE | call_stmt | ID |  LP numexpr1 RP ;


indexop 			: ID LSB indexlist RSB ;
indexlist			: numexpr1 COMMA indexlist | indexop COMMA indexlist | call_stmt COMMA indexlist 
					| indexop | numexpr1 | call_stmt;


indexed_array 		: LCB  ( exprlist | ) RCB ;




//Type
type_				: INTEGER | FLOAT | STRING | BOOLEAN | AUTO | array_type;

//Var declaration
var_declare			: id_list COLON type_ SEMI | ID recur expr SEMI;
recur				: COMMA ID recur expr COMMA | COLON type_ ASSIGN;

array_type			: ARRAY dimension OF type_ ;
dimension			: LSB intlist RSB ;
intlist				: numexpr1 COMMA intlist | numexpr1 ;
id_list				: ID COMMA id_list | ID ;


//function declarations
function_type		: type_ | VOID ;
param				: INHERIT? OUT? ID COLON ( type_ | ARRAY ) ;
param_list			: param COMMA param_list | param ;
func_declare		: ID COLON FUNCTION function_type LP ( param_list | ) RP (INHERIT ID)? block_stmt;

assignment			: (ID | indexop) ASSIGN expr;
return_stmt			: RETURN ( expr | ) ;
call_stmt			: ID LP argument RP ;
argument			: ID COMMA argument | expr COMMA argument | ID | expr | ;
if_stmt				: IF LP expr RP ( stmt ) ( ELSE stmt | );
for_stmt			: FOR LP ID ASSIGN numexpr1 COMMA expr COMMA numexpr1 stmt ;
while_stmt			: WHILE LP expr RP stmt  ;
do_while_stmt		: DO block_stmt WHILE LP expr RP;
block_stmt			: LCB (stmtlist |) RCB ;


/*Special function 
special_func 		: readInt | printInt | readFloat | writeFloat | readBool | printBool | readStr | printStr  | super | preventDef ;
readInt 			: READ_INT LP RP ;
printInt			: PRINT_INT LP expr RP ;
readFloat			: READ_FLOAT LP RP ;
writeFloat			: WRITE_FLOAT LP expr RP ;
readBool			: READ_BOOL LP RP ;
printBool			: PRINT_BOOL LP expr RP ;
readStr				: READ_STR LP RP ;
printStr			: PRINT_STR LP expr RP ;
//super				: SUPER LP exprlist RP ;
preventDef			: PREVENT_DEF LP RP ;
*/

/*Special function key
READ_INT			: 'readInteger' ;
PRINT_INT			: 'printInteger' ;
READ_FLOAT			: 'readFloat' ;
WRITE_FLOAT			: 'writeFloat' ;
READ_BOOL			: 'readBoolean' ;
PRINT_BOOL			: 'printBoolean' ;
READ_STR			: 'readString' ;
PRINT_STR			: 'printString' ;
//SUPER				: 'super' ;
PREVENT_DEF			: 'preventDefault' ;
*/

//Keywords
AUTO				: 'auto'  ;
BREAK				: 'break' ;
BOOLEAN				: 'boolean' ;
DO					: 'do' ;
ELSE				: 'else' ;
FALSE				: 'false' ;
FLOAT				: 'float' ;
FOR 				: 'for' ;
FUNCTION			: 'function' ;
IF					: 'if' ;
INTEGER				: 'integer' ;
RETURN 				: 'return' ;
STRING 				: 'string' ;
TRUE				: 'true' ;
WHILE				: 'while' ;
VOID 				: 'void' ;
OUT					: 'out' ;
CONTINUE			: 'continue' ;
OF 					: 'of' ;
INHERIT				: 'inherit' ;
ARRAY				: 'array' ;


//Operators
ADDOP				: '+' ;
SUBOP				: '-' ;
MULOP				: '*' ;
DIVOP				: '/' ;
MODULO				: '%' ;
LOGICNOT			: '!' ;
AND					: '&&';
OR 					: '||';
EQ					: '==';
NOTEQ				: '!=';
LESS				: '<' ;
LESSOREQ			: '<=';
MORE_				: '>' ;
MOREOREQ			: '>=';
DBLCOL				: '::';

//Seperators
LP					: '(' ;
RP					: ')' ;
LSB					: '[' ;
RSB					: ']' ;
DOT					: '.' ;
COMMA				: ',' ;
SEMI				: ';' ;
COLON				: ':' ;
LCB					: '{' ;
RCB					: '}' ;
ASSIGN				: '=' ;


COMMENT 			: '/*' .*? '*/' -> skip ;
LINE_COMMENT		: '//'  (~[\r\n])* -> skip	;



ID					: [A-Za-z_][A-Za-z0-9_]* ;
INT_TYPE			: INTPART {self.text = self.text.replace('_','')} ;
FLOAT_TYPE			: ( INTPART DECIMAL? EXPONENT | INTPART DECIMAL | DECIMAL EXPONENT   ) {self.text = self.text.replace('_','')} ;
fragment INTPART 	: '0' | [1-9] ('_'? [0-9]+)*  ;
fragment DECIMAL	: '.' [0-9]* ;
fragment EXPONENT	: [eE] [-+]? [0-9]+ ;
STRING_TYPE			:   '"''"' | '"'(~["'\n] | '\\t' | '\\r' | '\\n' | '\\b' | '\\f' | QUOTE | DBLQUOTE | BACKSLASH)*'"' {self.text=self.text[1:-1]};
fragment QUOTE 		: '\\''\u0027' ;
fragment DBLQUOTE 	: '\\''"' ;
fragment BACKSLASH 	: '\\''\\' ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR			: .  {raise ErrorToken(self.text)} ;

UNCLOSE_STRING		: '"' (~["\n])* {raise UncloseString(self.text)};	

ILLEGAL_ESCAPE		: '"'~["]*? ( '\n' | EOF ) ~["]*'"' {raise IllegalEscape(self.text)};