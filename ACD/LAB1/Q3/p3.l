%{


%}

lowCase				[a-z]
upCase				[A-Z]

%%
{lowCase}		{printf("%c",(((yytext[0]-97+5)%26)+97));}
{upCase}		{printf("%c",(((yytext[0]-65+5)%26)+65));}
. 						ECHO;
%%

int main()
{
	yylex();
	return 0;
}