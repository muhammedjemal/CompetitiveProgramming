class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = 0
        p = 0
        for i in range(len(nums)):
            for j in range(i, len(nums), 1):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
