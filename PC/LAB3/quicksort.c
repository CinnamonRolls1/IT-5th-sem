#include <stdio.h>
#include <omp.h>
#include <stdint.h>

void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

int part (int arr[], int low, int high)
{
	int pivot = arr[high];
	int i = low - 1;
	for(int j=low;j<=high-1;j++)
	{
		if (arr[j] < pivot)
		{
			i++;
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i+1], &arr[high]);
	return (i+1);
}
void qsort(int arr[], int low, int high)
{
	if (sizeof(arr)/sizeof(arr[0]) > 0)
	{
		if (low < high)
		{
			#pragma omp taskwait
			int pi =part(arr,low,high);
			#pragma omp task
			qsort(arr,low,pi-1);
			#pragma omp task
			qsort(arr,pi+1,high);
		}
	} 
	if (low < high)
	{
		int pi = part(arr,low,high);
		qsort(arr,low,pi-1);
		qsort(arr,pi+1,high);

	}
}

int main()
{
	float start,end;
	int arr[20];
	for(int i = 0;i<20;i++)
		arr[i] = 100-i;
	start = omp_get_wtime();
	qsort(arr,0,19);
	end = omp_get_wtime();
	printf("Time taken for recursive task parallelization = %f seconds\n", end-start);

	return 0;
}