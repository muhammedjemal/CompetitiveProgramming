class Solution(object):
    def shortestSubarray(self, nums, k):
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        res = len(nums)+1
        q = deque()
        for i, j in enumerate(prefix):
            while q and j <= prefix[q[-1]]:
                q.pop()
            while q and j - prefix[q[0]] >= k:
                res = min(res, i - q.popleft())
            q.append(i)
        return res if res < len(nums)+1 else -1
