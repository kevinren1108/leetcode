def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def merge(list1,list2):
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val < list2.val:
            list1.next = merge(list1.next, list2)
            return list1
        else:
            list2.next = merge(list1, list2.next)
            return list2
    
    res = ListNode(0)
    res = merge(list1, list2)
    return res
