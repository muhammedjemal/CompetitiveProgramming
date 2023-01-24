class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        res  = []
        
        for i,c in enumerate(s) :
            if c not in last :
                last[c] = [i,i]
            else :
                last[c][1] = i
        
        interval = list(last.items())[0][1]
        
        for _,[start,end] in list(last.items())[1:]:
            if start < interval[1] : 
                interval = [min(start,interval[0]),max(end,interval[1])]
            else :
                res.append((interval[1]-interval[0])+1)
                interval = [start,end]
                
        res.append((interval[1]-interval[0])+1) 
        return res
