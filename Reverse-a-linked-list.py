# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
 
class Solution:
   
    # Program to reverse the linked list
    # using stack
    def reverseLLUsingStack(self, head):
        
        # Initialise the variables
        stack, temp = [], head
         
        while temp:
            stack.append(temp)
            temp = temp.next
 
        head = temp = stack.pop()
         
        # Until stack is not
        # empty
        while len(stack) > 0:
            temp.next = stack.pop()
            temp = temp.next
 
        temp.next = None
        return head
 
# Driver Code
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3,
                        ListNode(4, ListNode(5)))))
    obj = Solution()
    head = obj.reverseLLUsingStack(head)
    while head:
        print(head.val, end=' ')
        head = head.next
