
class Solution:
    def minNonZeroProduct(self, p):
        pow1 = pow(2, p, 10**9 + 7)-1
        pow2 = pow(2,p-1)-1
        return (pow(pow1-1, pow2, 10**9 + 7)*pow1)%(10**9 + 7)
