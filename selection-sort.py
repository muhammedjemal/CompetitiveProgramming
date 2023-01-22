
class Solution: 
    def select(self, arr, i):
        # code here 
        for i in range(i,len(arr)):
            for j in range(i+1, len(A)):
                if A[i] > A[j]:
                 i = j
                 A[i], A[i] = A[i], A[i]
    
    def selectionSort(self, arr,n):
        #code here
         for k in range(n-1):
            for j in range(k+1, n):
                if arr[k] > arr[j]:
                    arr[k], arr[j] = arr[j], arr[k]
         return arr
