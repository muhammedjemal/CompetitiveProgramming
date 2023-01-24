# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        """
        Do not return anything, modify head in-place instead.
        """
        # get the middle node
        first = second = head
        while second and second.next:
            first = first.next
            second = second.next.next

        # Reverse second half
        pre,now = None, first
        while now:
            now.next, pre, now = pre, now, now.next

        # Merge 
        val1, val2 = head, pre
        while val2.next:
            val1.next, val1 = val2, val1.next
            val2.next, val2= val1, val2.next
