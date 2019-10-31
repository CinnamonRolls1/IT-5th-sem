%{
#include<stdio.h>
#include<stdlib.h>
	extern int yylex(); 
	
	void yyerror (char const *s) {
        fprintf (stderr, "%s\n", s);
    }
%}

%token ID NUM SWITCH CASE DEFAULT BREAK LE GE EQ NE AND OR IF THEN WHILE FOR DO
%right '='
%left AND OR
%left '<' '>' LE GE EQ NE
%left '+''-'
%left '*''/'
%right UMINUS
%left '!'

%%

S   :   ST{printf("\nInput accepted.\n");exit(0);};
    ;

ST  :   SWITCH'('ID')''{'B'}'
    ;

B   :   C
    |   C D
    ;

C   :   C C
    |   CASE NUM':'ST1 BREAK';'
    ;

D   :   DEFAULT':'ST1 BREAK';'
    |   DEFAULT':'ST1
    ;

ST1 :   WHILE'('E2')' E';'
    |   DO '{'E';''}' WHILE '('E2')'';'
    |   IF'('E2')'THEN E';'
    |   ST1 ST1
    |   FOR'('ASGN';'E2';'INC')' E';'   
    |   E';'
    ;

ASGN:   ID'='ID
    |   ID'='NUM
    ;

INC :   ID'+''+'
    |   ID'+''='NUM
    |   ID'-''='NUM
    |   ID'-''-'
    |   '+''+'ID
    |   '-''-'ID
    ;

E2  :   E'<'E
    |   E'>'E
    |   E LE E
    |   E GE E
    |   E EQ E
    |   E NE E
    |   E AND E
    |   E OR E
    ;

E   :   ID'='E
    |   E'+'E
    |   E'-'E
    |   E'*'E
    |   E'/'E
    |   E'<'E
    |   E'>'E
    |   E LE E
    |   E GE E
    |   E EQ E
    |   E NE E
    |   E AND E
    |   E OR E
    |   ID
    |   NUM
    |   '{'ST1'}'
    ;

%%

#include"lex.yy.c"

main()
{
    printf("\nEnter the expression: ");
    yyparse();
}