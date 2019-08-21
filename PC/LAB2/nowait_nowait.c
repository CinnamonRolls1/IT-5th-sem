#include <omp.h>
#include <stdio.h>
#include <math.h>

double sin_t(double x)
{
	double sin = x;
	double fact =1;
	int sign = -1;
	int i=0;
	for(i=1;i<50;i+=2)
	{
		fact = fact *(i+1)*(i+2);
		double term = sign * pow(x,i+2)/fact; 
		sin += term;

		sign*=-1;
	}

	return sin;
}

double cos_t(double x)
{
	double cos = 1;
	double fact =1;
	int sign = -1;
	int i=0;
	for(i=0;i<50;i+=2)
	{
		fact = fact *(i+1)*(i+2);
		double term = sign * pow(x,i+2)/fact; 
		cos += term;

		sign*=-1;
	}

	return cos;
}

int main()
{
	double x = 0;
	double y = 0;
	double z = 0;

	omp_set_num_threads(16);

	double beg = omp_get_wtime();
	#pragma omp parallel	
	{
		long int i = 0;
		#pragma omp for nowait 
		for(i = 0; i<1000 ;i++){
			y = cos_t(i);

		}

		long int j = 0;
		#pragma omp for nowait
		for(j =0; j<1000 ; j++){
			x = j*j;

		}


		long int k =0;
		#pragma omp single 
		for(k=0;k<1000;k++){
			z = sin_t(i);

		}

	}

	double end = omp_get_wtime();

	printf("Time taken %lf \n", end-beg);
	return 0;

}