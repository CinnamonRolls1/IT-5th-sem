#include<omp.h>
#include<stdio.h>
#include<stdlib.h>


#define m 500
#define n 500
#define n1 700



void mul(int arr[m][n],int brr[n][n1],int crr[m][n1],int l,int h)
{
  int count=0;
  for(int i=l;i<=h;i++)
  {
    for(int j=0;j<n1;j++)
     for(int k=0;k<n;k++)
       crr[i][j]=arr[i][k]*brr[k][j];
  }


}
void parallel_matrix(int arr[m][n],int brr[n][n1],int crr[m][n1],int l,int h,int size)
{
  int count=0;
  if((h-l+1)<=size)
  {
     mul(arr,brr,crr,l,h);
     return;

  }


  #pragma omp parallel sections
  {

    #pragma omp section
    parallel_matrix(arr,brr,crr,l,l+size-1,size);

    #pragma omp section
    parallel_matrix(arr,brr,crr,l+size,h,size);

  }


}
void Serial_matrix(int arr[m][n],int brr[n][n1],int crr[m][n1],int l,int h)
{
  mul(arr,brr,crr,l,h);
}

int main(int argc,char *argv[])
{
  int N;
  printf("Enter number of threads:");
  scanf("%d",&N);

  omp_set_num_threads(N);
  int A[m][n],B[n][n1],C[m][n1];
  int A1[m][n],B1[n][n1],C1[m][n1];
  int size=m/N;
  for(int i=0;i<m;i++)
  {
    for(int j=0;j<n;j++)
    {
      A[i][j]=i+j;
      A1[i][j]=A[i][j];
    }
  }
  for(int i=0;i<n;i++)
  {
    for(int j=0;j<n1;j++)
    {
      B[i][j]=i+j;
      B1[i][j]=B[i][j];
    }
  }
  for(int i=0;i<m;i++)
  {
    for(int j=0;j<n1;j++)
    {
      C[i][j]=0;
      C1[i][j]=0;
    }
  }


  printf("Start of Serial section...\n");
  double tm3=omp_get_wtime();
  Serial_matrix(A1,B1,C1,0,m-1);
  double tm4=omp_get_wtime();
  printf("End of Serial section!!\n");

  printf("Time Taken by Serial section:%lf sec\n",(tm4-tm3));

  printf("Start of Parallel section...\n");
  double tm1=omp_get_wtime();
  parallel_matrix(A,B,C,0,m-1,size);
  double tm2=omp_get_wtime();
  printf("End of Parallel section!!\n");

  printf("Time Taken by parallel section:%lf sec\n",(tm2-tm1));

  double s=(tm4-tm3)/(tm2-tm3);
  double p=(tm2-tm3)/(tm4-tm3);

  double speedup=1/(s+(p/N));
  printf("Speed up:%lf  number of threads:%d\n",speedup,N);

  return 0;
}
