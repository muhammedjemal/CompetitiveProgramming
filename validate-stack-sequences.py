class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i,j=0,0
        stack=[]
        n,m=len(popped),len(pushed)
        while j<len(pushed):
            stack.append(pushed[j])
            while len(stack)!=0 and i<n and stack[-1]==popped[i]:
                stack.pop()
                i=i+1
            j=j+1
        if len(stack)==0:
            return True
        else:
            return False
