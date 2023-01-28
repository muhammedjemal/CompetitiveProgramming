class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        nums2 = []
        for x in range(len(nums)):
            if nums[x] == target:
                nums2.append(x)
        return nums2
