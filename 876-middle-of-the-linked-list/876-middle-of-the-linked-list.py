# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        current=head
        
        while current:
            count+=1
            current=current.next
            
        n= count // 2
        oe= count % 2
        
        if oe == 0:
            for i in range(n ):
                head=head.next
        else:
            for i in range(n ):
                head=head.next
        
        return head