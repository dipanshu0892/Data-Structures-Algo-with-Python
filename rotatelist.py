# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        curr=head
        curr2=head
        l=[]
        while curr:
            l.append(curr.val)
            curr=curr.next
        n=len(l)
        j=n-1
        l2=[]
        i=0
        while j>i:
            l2.append(l[i])
            l2.append(l[j])
            i=i+1
            j=j-1

        if len(l)%2!=0:
            l2.append(l[i])

        for i in range(0,len(l2)):
            curr2.val=l2[i]

            curr2=curr2.next

