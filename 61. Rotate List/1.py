def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 0: return head
    if head.next == None: return head
    
    temp = head
    length = 1
    while temp.next:
        temp = temp.next
        length += 1
    
    k = k % length
        
    newHead = head
    for i in range (0,k):     
        list = head
        while head.next != None and k > 0:
            prev = head
            head = head.next
        prev.next = None        
        newHead = head
        newHead.next = list
        
    return newHead   

#### Another way: link the tail to head, cut at the k node from back
def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 0: return head
    if head.next == None: return head
    
    lastNode = head
    length = 1
    while lastNode.next:
        lastNode = lastNode.next
        length += 1
    
    k = k % length
    lastNode.next = head
    
    temp = head
    
    for i in range(0, length - k -1):
        temp = temp.next
    
    ans = temp.next
    temp.next = None
    
    
    return ans