from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    
    prev = head
    curr = head.next
    
    while curr and curr.next:
        nxt = curr.next

        prev.next = nxt
        curr.next = prev

        prev  = curr
        curr = nxt

    return prev

test = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
swapPairs(test)