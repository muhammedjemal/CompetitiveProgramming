class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            x = math.log(n,4)
            x = math.ceil(x)
            return n == pow(4, x)
