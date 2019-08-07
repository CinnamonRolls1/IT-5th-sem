#include <stdio.h>
#include <stdlib.h>
#include <omp.h>



static long num_steps = 100000;
double step;
int main()
{
	//time_t start,end;
	//time(&start); 
	double time_start = omp_get_wtime();
	double x, pi, sum = 0.0;
	step = 1.0/(double)num_steps;

	for(int i=0; i<num_steps;i++){
		x=(i+0.5)*step;
		sum=sum+4.0/(1.0+x*x);
	}

	pi=step*sum;
	printf("%f\n",pi);
	//time(&end);
	//double time_taken = double(end - start); 
	//cout << "Time taken by program is : " << fixed << time_taken << setprecision(5); 
	//cout << " sec " << endl; 
	double time_end = omp_get_wtime();
	printf("Elapsed time (sec) is %f\n",time_end-time_start);
    return 0; 
}