# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=[]
        ptr=l1
        cpt=l2
        while ptr:
            a.append(ptr.val)
            ptr=ptr.next
        while cpt:
            b.append(cpt.val)
            cpt=cpt.next
        a=a[::-1]
        b=b[::-1]
        a1 = ''.join([str(elem) for elem in a])
        b1=''.join([str(elem) for elem in b])
        c1=int(a1)+int(b1)
        c1=str(c1)
        c1=c1[::-1]
        c1=list(c1)
        h=[]
        for i in c1:
            h.append(int(i))
        print(h)
        dummy=ListNode(0)
        tpt=dummy
        for i in range(len(h)):
            dummy.next=ListNode(h[i])
            dummy=dummy.next
        return tpt.next


        