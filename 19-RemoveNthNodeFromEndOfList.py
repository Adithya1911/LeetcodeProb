# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None and n==1:
            return None
        tmp=head
        i=0
        while tmp:
            i+=1
            tmp=tmp.next
        if i==n:return head.next
        tmp=head
        for i in range(i-n-1):
            tmp=tmp.next
        tmp.next=tmp.next.next
        return head