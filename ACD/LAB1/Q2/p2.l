%{

int Pcount=0;
int Scount=0;
%}

%%
(p)(r)(i)(n)(t)(f)		{Pcount++;;printf("writef");}
(s)(c)(a)(n)(f)			{Scount++;;printf("readf");}
. 						ECHO;
%%

int main()
{
	yylex();
	printf("No. of printf %d\n", Pcount);
	printf("No. of scanf %d\n", Scount);
	
	return 0;
}