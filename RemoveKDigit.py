class Solution(object):
    def removeKdigits(self,num,k):
        stack=[]
        remain=len(num)-k
        for number in num:
            while k and stack and stack[-1]>number:
                stack.pop()
                k-=1
            stack.append(number)
        
        return ''.join(stack[:remain]).lstrip('0') or '0'
