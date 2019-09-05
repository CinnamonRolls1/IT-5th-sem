%{
	#include <stdio.h>

	int count=0;

%}
%%
[ \t\n]*ab[ \t\n]+ {count++;}
. {}
%%
int yywrap()
{
	return 1;
}

int main()
{
	yylex();
	printf("count: %d\n",count);

	return 0;
}