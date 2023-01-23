class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1,h2=l1,l2
        rem=0
        res=ListNode(None)
        restail=res
        while h1 or h2 or rem:
            val1=h1.val if h1 else 0
            val2=h2.val if h2 else 0
            summ=val1+val2+rem
            rem=summ//10
            
            restail.next=ListNode(summ%10)
            restail=restail.next
            h1=h1.next if h1 else None
            h2=h2.next if h2 else None
        return res.next
