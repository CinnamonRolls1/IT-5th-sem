#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(){
	int i;
	omp_set_num_threads(4);
	#pragma omp parallel 
	{
		
		i=omp_get_thread_num();
		printf("Hello World from %d\n",i);
	}
}
