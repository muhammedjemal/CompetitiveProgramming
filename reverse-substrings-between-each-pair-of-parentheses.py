class Solution:
    def reverseParentheses(self, s: str) -> str:
        arr = [""]
        for value in s:
            if value == '(':
                arr.append('')
            elif value == ')':
                add = arr.pop()[::-1]
                arr[-1] += add
            else:
                arr[-1] += value
        return arr.pop()
