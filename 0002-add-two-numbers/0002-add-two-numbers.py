# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        d=dummy=ListNode()
        
        while l1:
            s1=str(l1.val) + s1
            l1=l1.next
            
        while l2:
            s2= str(l2.val) + s2
            l2= l2.next
            
        sum_=int(s1) + int (s2)
        sum_s=str(sum_)
        
        for i in sum_s[::-1]:
            d.next=ListNode(int(i))
            d=d.next
            
        return dummy.next