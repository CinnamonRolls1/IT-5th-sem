%{

int count;
%}

comment				[/\*{.*|\n}\*/] 


%%
{comment}			{count++;}
%%

int main()
{
	yylex();
	printf("No. of comments: %d\n", count);
	return 0;
}