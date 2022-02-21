def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    try:
        fast = head.next
        slow = head
        while fast != slow:
            fast = fast.next.next
            slow = slow.next
    except:
        return None
    
    slow = slow.next
    while head != slow:
        head = head.next
        slow = slow.next
    
    return head