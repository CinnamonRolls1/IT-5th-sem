%{#include<stdio.h>
int a=0,b=0,c=0,d=0,ob=0,cb=0;
int flaga=0,flagb=0,flagc=0,flagd=0;
%}

%%
[a-zA-z]+ printf("\n %s is an identifier\n",yytext);
[+] {a++;flaga=1;}
[-] {b++;flagb=1;}
[*] {c++;flagc=1;}
[/] {d++;flagd=1;}
[(] ob++;
[)] cb++;
%%

int yywrap()
{
	return 1;
}

main()
{
printf("Enter expression:");
yylex();
if(ob==cb)
printf("\nValid expression\n");
else
printf("Invalid expression\n");
printf("Addition=%d\tSubtract=%d\nMultiply=%d\tDivide=%d\n",a,b,c,d);
printf("\n Operators used:\n");
if(flaga==1)
printf("+\n");
if (flagb==1)
printf("-\n");
if(flagc==1)
printf("*\n");
if(flagd==1)
printf("/\n");
}