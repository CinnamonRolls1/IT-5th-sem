#include <omp.h>
#include <stdio.h>
static long num_steps = 100000;
double step;
#define NUM_THREADS 2
void main ()
{
	int i, nthreads; double pi, sum[NUM_THREADS];
	step = 1.0/(double) num_steps;
	omp_set_num_threads(NUM_THREADS);
	double time_start = omp_get_wtime();
	#pragma omp parallel
	{
		int i, id,nthrds;
		double x,wt;
		id = omp_get_thread_num();
		nthrds = omp_get_num_threads();
		//printf("%d\n",nthrds );
		wt=omp_get_wtime();
		//printf("Wtime = %lf\n",wt);
		if (id == 0) nthreads = nthrds;

		for (i=id, sum[id]=0.0;i< num_steps; i=i+nthrds)
		{
			#pragma omp critical
			x = (i+0.5)*step;
			sum[id] += 4.0/(1.0+x*x);
		}

	}
	for(i=0, pi=0;i<nthreads;i++)pi += sum[i] * step;
	double time_end = omp_get_wtime();
	printf("Elapsed time (sec) is %f\n",time_end-time_start);
	printf("%lf\n",pi);
}