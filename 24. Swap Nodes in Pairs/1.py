# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2 -> 4 -> 5 -> 8 -> 10 -> 6
#
#
#
#
# 4 -> 2 -> 8 -> 5 -> 6 -> 10
# def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
#     if not head or not head.next:
#         return head
#     #prev node, now the prev point to 1
#     prev = head
#     #move to next node， curr point to 2
#     curr = prev.next
#     #save curr's next, nxt point to 3
#     nxt = curr.next
#     # 2 -> 1
#     curr.next = prev
#     # 1 -> 3
#     prev.next = swapPairs(nxt)
#     return curr

# 2 -> 4 -> 5 -> 8 -> 10 -> 6
#
#
#
#
# 4 -> 2 -> 8 -> 5 -> 6 -> 10
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    

    dummy = ListNode(-1)
    dummy.next = head

    prev = dummy

    while head and head.next:
        first, second = head, head.next

        prev.next = second

        first.next = second.next
        second.next = first

        prev = first
        head = head.next

    return dummy.next

def printList(head: Optional[ListNode]):
    res = ""
    if not head:
        return head
    while head.next:
        res += str(head.val) + " -> "
        head = head.next
    if head:
        res += str(head.val)
    return res

testList = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode (5, ListNode(6, None))))))

print(printList(testList))
testList = swapPairs(testList)
print(printList(testList))