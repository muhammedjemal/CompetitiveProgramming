class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1 = []
        dick = {"+","-","*","/"}

        for ele in tokens :
            if not ele in dick:
                stack1.append(int(ele))
            else:
                if stack1:
                    n1 = stack1.pop()
                    n2 = stack1.pop()
                    ans = eval(str(n2)+ele+str(n1))

                stack1.append(int(ans))

        return stack1[0]
