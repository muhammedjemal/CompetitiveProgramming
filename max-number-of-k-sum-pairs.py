class Solution:
    def maxOperations(self, A, K):
        A.sort()
        ans, l, r = 0, 0, len(A) - 1
        while l < r:
            val = A[l] + A[r]
            if val <= K: l += 1
            if val >= K: r -= 1
            if val == K: ans += 1
        return ans
