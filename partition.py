import random

def partition(A, low, high):
  
  pivot = A[L]  
  L=low
  R=high

  while L < R:
    while L < R and A[L] <= pivot:
      L += 1

    while L < R and A[R] > pivot:
      R -= 1

    if L < R:
      A[L], A[R] = A[R], A[L]

  A[low], A[R] = A[R], A[low]  

  return R  

def quickSort(A, L, R):
    
    if L < R:   
        partition_index = partition(A, L, R) #a[p_i] is at the right place in Aay

        quickSort(A, L, partition_index - 1);  
        quickSort(A, partition_index + 1, R); 


#example usage
A = random.sample(string.ascii_lowercase, 10) #100 letters

print("Original Array:", A)
quickSort(A, 0, len(A) - 1)
print("QuickSort:", A)
