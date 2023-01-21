class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones , twos, zeros = 0,0,0
        for x in range(len(nums)):
            if nums[x] == 0:
                zeros += 1
            elif nums[x] == 1:
                ones += 1
            elif nums[x] == 2:
                twos += 1
        nums.clear()
        nums.extend([0] * zeros)
        nums.extend([1] * ones)
        nums.extend([2] * twos)
                
        return nums
