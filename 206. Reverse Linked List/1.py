# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # 2 - 3 - 4 - 5 - 6
#
#   Itration
#
#
# def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
#     prev = None
#     curr = head
#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#     return prev


# 2 -> 3 -> 4 -> 5 -> 6 to 6 -> 5 -> 4 -> 3 -> 2 -> None 
#
#   recursive
#
#
def helper(curr, prev):
    if not curr : return prev
    nxt = curr.next
    curr.next = prev
    return helper(nxt, curr)

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    return (helper(head, None))

def printList(head: Optional[ListNode]):
    while head:
        print(str(head.val) + ",") if head.next else print(str(head.val))
        head = head.next

testList = ListNode(2,ListNode(4, ListNode(5, ListNode(8, ListNode (10, None)))))

testList = reverseList(testList)
printList(testList)
