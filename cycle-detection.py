def has_cycle(head):
    fast = head
    if head == None:return 0
    while fast and fast.next:
        head = head.next
        fast = fast.next.next
        if fast==head:return 1
    return 0
