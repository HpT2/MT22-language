grammar MT22;

@lexer::header {
#2012385
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;


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

ID			: [A-Za-z_][A-Za-z0-9_]* ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;