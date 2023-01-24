# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        count=0
        while(current):
            current=current.next
            count=count+1
        
        middle=(count//2)
        middlenode=head
        while(middle):
            # if node
            middlenode=middlenode.next
            middle=middle-1
        return middlenode
        # for i in range(middle):
