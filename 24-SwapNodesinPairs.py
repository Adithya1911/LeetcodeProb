# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp=head
        l=[]
        while tmp:
            l.append(tmp.val)
            tmp=tmp.next
        if len(l)%2==0:
            for i in range(0,len(l),2):
                temp=l[i]
                l[i]=l[i+1]
                l[i+1]=temp
        else:
            for i in range(0,len(l)-1,2):
                temp=l[i]
                l[i]=l[i+1]
                l[i+1]=temp
        tmp=head
        i=0
        while tmp:
            tmp.val=l[i]
            i+=1
            tmp=tmp.next
        return head
    