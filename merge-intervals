class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        nums = []
        for x in intervals:
            if not nums or nums[-1][-1] < x[0]:
                nums.append(x)
            else:
                nums[-1][-1] = max(nums[-1][-1], x[-1])
        return nums
