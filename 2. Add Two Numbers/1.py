from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeList(arr):
	for i in arr:
		x = ListNode(i)
		x = x.next
	return x

l1 = makeList([2,4,3])
l2 = makeList([5,6,4])
# 			  [7,0,8]
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
	temp = result = ListNode(0, None)
	carrier = 0
	while l1 or l2 or carrier:
		cur1 = 0
		cur2 = 0
		
		if l1:
			cur1 = l1.val
			l1 = l1.next
		if l2:
			cur2 = l2.val
			l2 = l2.next
		sum = cur1 + cur2 + carrier

		if sum > 9:
			sum = sum - 10
			carrier = 1
		else:
			carrier = 0

		result.next = ListNode(sum)
		result = result.next

	return temp.next

addTwoNumbers(l1,l2)