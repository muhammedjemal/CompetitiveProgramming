class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        arr=[]
        for i in matrix:
            arr=[*arr,*i]
        return sorted(arr)[k-1]
