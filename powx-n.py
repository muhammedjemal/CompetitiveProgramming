class Solution:
    def myPow(self, x: float, n: int) -> float:
        #approach1
        #return x**n

        #approach2 recursive 
        if n == 1:
            return x
        elif n == 0:
            return 1
        elif n == -1:
            return 1 / x

        broken=Solution.myPow(self,x,n//2)
        if(n%2==0):
            return broken*broken
        elif n%2!=0:
            return broken*broken*x
        elif n<-1:
            return broken*broken//2
