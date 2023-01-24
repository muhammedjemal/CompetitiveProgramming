class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        j = 0
        result = 0
        for i in range(len(s)):
            
            if s[i] not in visited:
                result = max(result,i-j+1)
            
            else:
                if visited[s[i]] < j:
                    result = max(result,i-j+1)
                else:
                    j = visited[s[i]] + 1
            visited[s[i]] = i
        return result
