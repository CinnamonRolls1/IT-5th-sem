#include <stdio.h>
#include <omp.h>
 

int fib(int n) 
{ 
	if (n <= 1) 
		return n; 
	return fib(n-1) + fib(n-2); 
} 
  
int main() 
{ 
	int n = 30; 
	double beg=omp_get_wtime();
	printf("%d", fib(n)); 
	// getchar(); 
	double end=omp_get_wtime();
	printf("\nTime taken:%f\n", end-beg);
	return 0; 
} 