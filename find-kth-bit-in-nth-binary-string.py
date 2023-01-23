class Solution:
    def reverse(self,n):
        return n[::-1]
    def invert(self, n):
        answer=''.join(['1' if i == '0' else '0'
                     for i in n])
        return answer
    def solution(self,n):
        if(n==1):
            return "0"
        else:
            return self.solution(n-1)+"1"+self.reverse(self.invert(self.solution(n-1)))
    def findKthBit(self, n: int, k: int) -> str:
        ans='0'
        while n > 1:
            ans+= '1' + ''.join('1'if i=='0'else '0' for i in ans)[::-1]
            n-=1
        return ans[k-1]
