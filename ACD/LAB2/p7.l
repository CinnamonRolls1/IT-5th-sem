%{
#include <stdio.h>
#include <string.h>
char* ids[100];
int top =0;
int key_count=0;
int id_count=0;
int op[5];//0-> +,1-> -,2-> *, 3-> / 4-> =

void inc_opr(char opr[])
{
	//printf("opr= %c\n",opr[0]);
	if(opr[0] == '+')
	{
		op[0]++;
	}
	if(opr[0] == '-')
	{
		op[1]++;
	}
	if(opr[0] == '*')
	{
		op[2]++;
	}
	if(opr[0] == '/')
	{
		op[3]++;
	}
	if(opr[0] == '=')
	{
		op[4]++;
	}

}




%}

operator "+"|"-"|"*"|"/"|"="
id ^[a-zA-Z][_a-zA-Z0-9]*$
keywords "int"|"float"|"char"|"double"|"do"|"if"|"continue"|"void"|"switch"|"return"|"else"

%%

{operator} {inc_opr(yytext);printf("%s\n",yytext);}
{keywords} {key_count+=1;printf("%s\n",yytext);}
{id}  {id_count+=1;}

. {}
%%

int yywrap()
{
	return 1;
}

int main()
{
	yylex();
	printf("No of + %d \n",op[0]);
	printf("No of - %d \n",op[1]);
	printf("No of * %d \n",op[2]);
	printf("No of / %d \n",op[3]);
	printf("No of = %d \n",op[4]);
	printf("No of keywords %d\n",key_count);
	printf("No of identifiers %d\n", id_count);

}
