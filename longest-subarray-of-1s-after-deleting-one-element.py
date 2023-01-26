
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        zeros = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1
                if zeros >= 2:
                    while zeros > 1:
                        if nums[i] == 0:
                            zeros -= 1
                        i+=1
            ans = max(ans,j-i)
        return ans
