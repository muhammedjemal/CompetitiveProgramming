class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace("()", '').replace("[]", "").replace('{}', '')
        if len(s) == 0:
            return True 
        else: 
            return False
