

%{
#include<stdio.h>

char* longest;
%}

longest     [a-zA-Z0-9]+[ |\n]

%%



{longest}   {
            if (yyleng > strlen(longest)) {
                longest = (char*)realloc(longest, yyleng + 1);
                strcpy(longest, yytext);
            }
        }
<*>.|\n    

%%

int main() {
    longest = (char*)malloc(1);
    longest[0] = '\0';
    yylex();
    printf("Longest string is '%s'\n", longest);
    int len = strlen(longest);
    printf("Length: %d\n", --len);
    printf("Reversed: ");
	
	for(int i=len-1; i>=0; i--){
		printf("%c", longest[i]);
	}
	printf("\n");
	free(longest);
    return 0;
}