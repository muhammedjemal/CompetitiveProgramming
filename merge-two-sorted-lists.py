class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        current=result        

        while list1 != None and list2 != None:
            if list1.val>list2.val:
                current.next=list2
                list2=list2.next
            else:
                current.next=list1
                list1=list1.next
            current=current.next
        
        if list1 != None:
            current.next=list1
        else:
            current.next=list2
        
        return result.next
