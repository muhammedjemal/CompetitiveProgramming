class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if (nums==None):
            return 0
        result=0
        temp=0
        nums.sort()
        pre=nums[0]
        for i in range(1,len(nums)):
            temp=pre+1
            result+=max(temp-nums[i],0)
            pre=max(temp,nums[i])
        return result
