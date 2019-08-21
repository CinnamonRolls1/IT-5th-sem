#include <iostream>
using namespace std;
#include <omp.h>

#define LEN 512

void mat_mult(double a[][LEN], double b[][LEN],double c[][LEN], int m, int n, int p)
{
	for(int i=0;i<m;i++)
	{
		
		for(int j=0;j<n;j++)
		{
			c[i][j] = 0;

			for(int k=0;k<p;k++)
			{
				c[i][j] += a[i][k]*b[k][j];
			}
		}
	}
}

int main(int argc, char const *argv[])
{
	
	double a[LEN][LEN],b[LEN][LEN],c[LEN][LEN];

	int m=LEN;
	int n=LEN;
	int p=LEN;

	int count = 0;
	for (int i = 0; i < LEN; ++i)
	{
		for (int j = 0; j < LEN; ++j)
		{
			a[i][j] = ++count;
			b[i][j] = count;
		}
	}
	

	double beg = omp_get_wtime();
	mat_mult(a,b,c,m,n,p);
	double end = omp_get_wtime();


	// for(int i=0;i<m;i++)
	// {
	// 	for(int j=0;j<n;j++)
	// 	{
	// 		cout<<c[i][j]<<' ';
	// 	}
	// 	cout<<endl;
	// }

	cout<<"Time Taken: "<<end-beg<<endl;

	return 0;
}