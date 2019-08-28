#include <stdio.h>
#include <omp.h>

void Qsort(int sercopy[25], int first, int last) {
  int pivot, i_pivot, temp, left, right;
  if (first >= last) return; 

   i_pivot = (first + last) / 2;
   pivot = sercopy[i_pivot];
   left = first; 
   right = last;
   while (left <= right) {
      if (sercopy[left] > pivot) { 
         temp = sercopy[left]; 
         sercopy[left] = sercopy[right]; 
         sercopy[right] = temp;
         if (right == i_pivot) {
            i_pivot = left;
         }
      right--;
      } 
      else { 
         left++;
      }
   }

   temp = sercopy[right];
   sercopy[right] = pivot;
   sercopy[i_pivot] = temp;


   Qsort(sercopy, first, (right - 1));
   Qsort(sercopy, (right + 1), last);

}

int main(){
   int count=50;
   for (int j = 0; i < count; ++i)
   {
      /* code */
   }

   printf("Enter %d elements: ", count);
   for(int i=0;i<count;i++)
      scanf("%d",&sercopy[i]);
   double s_beg=omp_get_wtime();
   Qsort(sercopy,0,count-1);
   double s_end=omp_get_wtime();

   printf("Serial output:\n");
   for(i=0;i<count;i++)
      printf(" %d",sercopy[i]);

   printf("\nTime taken: %f\n", s_end-s_beg);

   // double p_beg=omp_get_wtime();
   // serial_quicksort(sercopy,0,count-1);
   // double p_end=omp_get_wtime();
   return 0;
}