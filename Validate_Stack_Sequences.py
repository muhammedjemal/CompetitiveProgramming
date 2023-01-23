class Solution(object):
    def validateStackSequences(self,pushed,popped):
        stack=[]
        index=0
        for push_value in pushed:
            stack.append(push_value)
            while stack and stack[-1]==popped[index]:
                stack.pop()
                index+=1
        return not stack
            
