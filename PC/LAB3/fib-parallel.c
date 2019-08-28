#include <stdio.h>
#include <omp.h>
 

int fib_para(int n) 
{ 
	if (n <= 1) 
		return n; 
	int a,b;

	if (n<20){
		return fib_para(n-1)+fib_para(n-2);
	}

	else{

	#pragma omp task shared(a) 
	{
		a=fib_para(n-1);
	}
	#pragma omp task shared(b) 
	{
		b=fib_para(n-2);
	}
	return a + b; }
} 

int fib_para_taskwait(int n) 
{ 
	if (n <= 1) 
		return n; 
	int a,b;

	if (n<20){
		return fib_para_taskwait(n-1)+fib_para_taskwait(n-2);
	}

	else{

	#pragma omp task shared(a) 
	{
		a=fib_para_taskwait(n-1);
	}
	#pragma omp task shared(b) 
	{
		b=fib_para_taskwait(n-2);
	}
	#pragma omp taskwait
	return a + b; }
} 

int fib_ser(int n) 
{ 
	if (n <= 1) 
		return n; 
	return fib_ser(n-1) + fib_ser(n-2); 
} 
  
int main() 
{ 
	int n = 30; 

	omp_set_num_threads(4);
	double s_beg=omp_get_wtime();
	printf("\n%d", fib_ser(n));
	double s_end=omp_get_wtime();
	printf("\nTime taken for serial:%f\n", s_end-s_beg);

	double p_beg=omp_get_wtime();
	printf("\n%d", fib_para(n));
	double p_end=omp_get_wtime();
	printf("\nTime taken for parallel:%f\n", p_end-p_beg);

	double p_t_beg=omp_get_wtime();
	printf("\n%d", fib_para_taskwait(n));
	double p_t_end=omp_get_wtime();
	printf("\nTime taken for parallel (taskwait):%f\n", p_t_end-p_t_beg);
	return 0; 
} 
	
