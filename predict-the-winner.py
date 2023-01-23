class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        if len(nums)%2==0:
            return True
        lst=nums[:]
        for i in range(1,len(nums)):
            for j in range(len(nums)-i):
                lst[j]=max(nums[j]-lst[j+1],nums[j+i]-lst[j])
        if lst[0]>=0:
            return True
        else:
            return False
