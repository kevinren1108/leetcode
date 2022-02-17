from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	res = curr =  ListNode(0,None)
	while list1 and list2:
		if list1.val < list2.val:
			curr.next = list1
			list1 = list1.next
		else:
			curr.next = list2
			list2 = list2.next
		curr = curr.next
	
	curr.next = list1 or list2
			
	
	return res.next

list13 = ListNode(3,None)
list12 = ListNode(2,list13)
list11 = ListNode(1,list12)

list23 = ListNode(4,None)
list22 = ListNode(3,list23)
list21 = ListNode(1,list22)

print('ans')
print(mergeTwoLists(list11,list21))