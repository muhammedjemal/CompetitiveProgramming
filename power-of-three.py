class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        y = math.log(n , 3)
        y = math.ceil(y)
        return math.pow(3, y) == n
