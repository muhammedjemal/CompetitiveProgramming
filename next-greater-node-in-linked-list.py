# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    
        result = []
        stack = []
        i,n = 0,0
        length = head
        
        while(length):
            n+=1
            length = length.next
        result=[0]*n
        while(head):
            while(stack and stack[-1][1] < head.val):
                index, _ = stack.pop()
                result[index] = head.val
            stack.append([i, head.val])
            i += 1
            head = head.next
        return result
