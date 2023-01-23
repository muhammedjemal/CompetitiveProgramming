# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        count = n
        while fast:
            if count < 0:
                slow = slow.next
            count -= 1
            fast = fast.next
        if count == 0:
            return head.next
        slow.next = slow.next.next
        return head
