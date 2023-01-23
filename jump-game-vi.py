class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = [0]
        i = 1
         
        while i < len(nums):
            if (n[0] + k) < i:
                n.pop(0)
            nums[i] += nums[n[0]]
            while len(n) > 0 and nums[n[-1]] <= nums[i]:
                n.pop()
            n.append(i)
            i += 1
        return nums.pop()
