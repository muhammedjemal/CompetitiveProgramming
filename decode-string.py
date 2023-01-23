class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        result=""
        number=0
        for i in s:
            if i.isdigit():
                number = number*10 + int(i)
            elif i.isalpha():
                result += i
            elif i == "[":
                stack.append(result)
                stack.append(number)
                result = ''
                number = 0
            elif i == ']':
                previous_num = stack.pop()
                previous_string = stack.pop()
                result = previous_string + previous_num * result
        return result
                
