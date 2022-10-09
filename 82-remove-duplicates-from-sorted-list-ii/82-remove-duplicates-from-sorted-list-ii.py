# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        dummy=ListNode()
        d=dummy
        
        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current=current.next
                    
                d.next=current.next
                    
            else:
                d.next=current
                d=d.next
                
            current=current.next
            
        return dummy.next