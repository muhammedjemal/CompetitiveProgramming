class Solution:
    def deleteDuplicates(self, head):
        hd = head
        temp = []
        preceding = None

        while hd is not None:
            if hd.val in temp:
                preceding.next = hd.next
            else:
                temp.append(hd.val)
                preceding = hd

            hd = preceding.next    
        return head
