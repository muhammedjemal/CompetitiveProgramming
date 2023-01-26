class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        accumulator = 1
        for i in nums:
            result.append(accumulator)
            accumulator *= i
        accumulator = 1
        for n in reversed(range(len(nums))):
            result[n] *= accumulator
            accumulator *= nums[n]   
        return result
