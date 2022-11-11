# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        d={}
        while head:
            if head.val not in d:
                d[head.val]=1
            else:
                d[head.val] +=1
                
            head=head.next
            
        for i,j in d.items():
            if j == 1:
                a.append(i)
                
        
        
        d=dummy=ListNode()
        
        for i in a:
            d.next=ListNode(i)
            d=d.next
            
        return dummy.next