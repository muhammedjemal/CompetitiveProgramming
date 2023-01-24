# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        now = prev = ListNode(None) 
        now.next =  temp
        while temp and temp.next:
            if temp.val == temp.next.val: 
                while(temp and temp.next and temp.val == temp.next.val): 
                    temp = temp.next   
                temp = temp.next
                prev.next = temp 
            else: 
                prev = prev.next
                temp = temp.next

        return now.next
