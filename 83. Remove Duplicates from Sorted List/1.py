def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #variabbles:  preVal,currVal
    #printers:    prev,curr
    if not head: return head
    if not head.next: return head
    
    prev = ListNode(-111,None)
    curr = head
    
    preVal = prev.val
    currVal = curr.val
    
    while curr.next:
        if currVal == preVal:
            prev.next = curr.next
            
            preVal = prev.val
            currVal = curr.val
            
            prev = curr
            curr = curr.next
            
        else:
            prev = curr
            curr = curr.next
            
    return head       