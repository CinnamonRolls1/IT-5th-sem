%{
	#include <stdio.h>
	char *replace = "zebra";

%}

item horse
%%

{item} {printf("%s",replace);}
. ECHO;

%%

int yywrap()
{
	return 1;
}

int main()
{
	yylex();
	return 0;
}