class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key= lambda x:x[-1])
        curr = 0
        res = ""
        while curr < int(s[-1][-1]):
            res += s[curr][:-1]
            if curr != int(s[-1][-1]) -1:
                res += " "
            curr += 1
        return res
