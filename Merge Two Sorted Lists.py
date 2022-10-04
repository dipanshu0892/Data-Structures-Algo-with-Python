def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:  # If both lists empty - return None
            return None
        if not l1 or not l2:  # If one of the lists empty - return the other list
            return l1 or l2
        if l1.val < l2.val:  # If first ll val is lower - return new Node with this value and recursively merge ll's without first element in first ll 
            return ListNode(val=l1.val, next=self.mergeTwoLists(l1.next, l2))
        else:  #  If second ll val lower or equal - same step as before, but without first element in second ll
            return ListNode(val=l2.val, next=self.mergeTwoLists(l1, l2.next))
