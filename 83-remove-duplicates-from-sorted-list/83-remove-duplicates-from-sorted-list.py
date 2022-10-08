# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=head
        if head:
            current=head.next
        
            while current:
                if pre.val == current.val:
                    pre.next=current.next
                    current=current.next

                else:
                    pre=current
                    current=current.next

        return head