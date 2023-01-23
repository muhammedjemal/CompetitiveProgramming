class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        l=[]
        for i in range (len(temperatures)-1,-1,-1):
            while stack:
                if temperatures[i]<temperatures[stack[-1]]:
                    l.append(stack[-1]-i)
                    stack.append(i)
                    break
                else:
                    stack.pop()
            else:
                l.append(0)
                stack.append(i)
        return l[::-1]
