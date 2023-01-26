class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        preference=list(accumulate([0 if num%2==0 else 1 for num in nums]))
        dict_=defaultdict(int)
        result=0
        dict_[0]=1
        for num in preference:
            if num-k in dict_:
                result+=dict_[num-k]
            dict_[num]+=1
        return result
