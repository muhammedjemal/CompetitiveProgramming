class Solution:
    def longestSubarray(self, nums, limit):
        min_=[]
        max_=[]
        n=len(nums)
        result=0
        i=0
        for j in range(n):
            while min_ and min_[-1] > nums[j]:
                min_.pop()
            min_.append(nums[j])
            while max_ and max_[-1] < nums[j]:
                max_.pop()
            max_.append(nums[j])
            
            if max_[0] - min_[0] <= limit:
                result = max(result, j-i+1)
            else:
                if max_[0] == nums[i]:
                    max_.pop(0)
                if min_[0] == nums[i]:
                    min_.pop(0)
                i= i+ 1
        return result
