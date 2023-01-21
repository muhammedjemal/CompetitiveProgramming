class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            check = nums[l[i]:r[i]+1]
            check.sort()
            val = check[0]-check[1]
            flag = True
            for x,y in itertools.pairwise(check):
                if x-y != val:
                    flag = False
            ans.append(flag)
        return ans
