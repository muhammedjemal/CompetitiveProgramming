class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        firstsum = 0
        window_start = 0
        n = len(cardPoints)
        window_end = n-k
        
        for i in range(window_end,n):
            firstsum += cardPoints[i]
        ans = firstsum
        for window_end in range(n-k,n):
            firstsum += cardPoints[window_start] - cardPoints[window_end]
            ans = max(ans,firstsum)
            window_start += 1
        return ans
