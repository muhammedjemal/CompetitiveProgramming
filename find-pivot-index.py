class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
       
        pivot = 0
        sum2 = 0
        total =0

        for i in nums:
            total += i
       
        while pivot < len(nums):
            temp =  nums[pivot] + sum2
            sum1 = total - temp 
            if sum1 == sum2:
                return  pivot
            else:
                sum2 += nums[pivot]
            pivot +=1
        return  -1
