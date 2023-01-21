class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums2 =[]
        nums3 = []
        for x in nums:
            x = int(x)
            nums2.append(x)
        nums2.sort()
        return str(nums2[len(nums2)-k])
