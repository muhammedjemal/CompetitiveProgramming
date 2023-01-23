class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr , i, count = [i for i in range(1, n+1)], 0, 1
        while len(arr) > 1:
            if count == k:
                arr.pop(i)
                count = 1
            else:
                i+=1
                count += 1
                i = i % len(arr)
                
        return arr[0]
