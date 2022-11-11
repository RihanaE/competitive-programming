# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        
        pre=head
        current=head.next
        d=dummy=ListNode()
        
        while current:
            if pre.val == current.val:
                while current and pre.val == current.val:
                    pre=current
                    current=current.next
                    
                pre=current
                if current:
                    current=current.next
                d.next=pre   
                
            else:
                d.next=pre
                pre=current
                current=current.next
                d=d.next
                
        return dummy.next