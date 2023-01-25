class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        def sums(arr,k):
            start=0
            currsum=0
            n=len(arr)
            result=[0]*(n-k+1)
            for end in range(n):
                currsum+=arr[end]
                while end-start==k-1:
                    result[start]=currsum/k
                    currsum-=arr[start]
                    start+=1
            return result
        count=0
        for i in sums(arr,k):
            if i>=threshold:
                count+=1
        return count
