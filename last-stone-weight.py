class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) ==1:
            return stones[0]
        
        while(len(stones)>1):
            stones.sort(reverse=True)
            y=stones.pop(0)
            x=stones.pop(0)
            difference=y-x
            if(difference!=0):
                y=abs(y-x)
                stones.append(y)
            stones.sort()
        if len(stones) ==0:
            return 0
        else:
            return stones[0]
