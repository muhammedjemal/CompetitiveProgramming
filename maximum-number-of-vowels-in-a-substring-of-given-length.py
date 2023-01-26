class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        answer = cnt = 0
        for idx, char in enumerate(s):
            if char in vowels:
                cnt += 1
            if idx >= k and s[idx - k] in vowels:
                cnt -= 1
            answer  = max(cnt, answer)
        return answer
