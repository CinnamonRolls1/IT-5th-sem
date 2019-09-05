%{
	#include <stdio.h>
	int f=0;
%}

%%
.(""[aA][nN][dD]"")|(""[oO][rR]"")|(""[bB][uU][tT]""). {f=1;}
. {}

%%

int yywrap()
{
	return 1;
}

int main()
{
	yylex();
	if(f==0){printf("Simple\n");}
	if(f==1){printf("Complex\n");}
	return 0;
}
