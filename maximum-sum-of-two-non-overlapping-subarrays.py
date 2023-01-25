
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
#         [0,6,5,2,2,5,1,9,4]

        prefix = [0]
        ans = 0
    
        for i in nums:
            prefix.append(prefix[-1] + i)
            
        for j in range(2):
            left = 0
            
            for i in range(firstLen + secondLen, len(nums) + 1):
                left = max(left, prefix[i - firstLen] - prefix[i-secondLen-firstLen])
                ans = max(ans, left + prefix[i] - prefix[i-firstLen])
                
            firstLen, secondLen = secondLen, firstLen 
            
        return ans
