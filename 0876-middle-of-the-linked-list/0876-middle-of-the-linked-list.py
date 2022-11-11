# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size=0
        current=head
        
        while current:
            size +=1
            current=current.next
            
        mid=(size // 2) 
        
        for i in range(mid):
            head=head.next
            
        return head