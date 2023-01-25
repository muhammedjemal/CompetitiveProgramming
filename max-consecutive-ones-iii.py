class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,longest = 0,0,0
        freqs = {}
        while r < len(nums):
            if(nums[r] in freqs):
                freqs[nums[r]] += 1
            else:
                freqs[nums[r]] = 1 
            while 0 in freqs and freqs[0] > k:
                freqs[nums[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
            r += 1
        return longest
