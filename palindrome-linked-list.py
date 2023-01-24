# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        while(head):
            result.append(head.val)
            head=head.next
        return result == result[::-1]
