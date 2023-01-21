class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2 = []
        for x in range(len(nums)):
            count = 0
            for y in range(len(nums)):
                if nums[x] > nums[y] and nums[x] != nums[y]:
                    count += 1

            nums2.append(count)
            
        print (nums2)
        return nums2
