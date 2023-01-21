class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        i = 0
        counter = 0
        length = len(nums)
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                length -= 1
                i -= 1
                counter += 1
            i +=1
        for x in range(counter):
            nums.append(0)
        return nums
