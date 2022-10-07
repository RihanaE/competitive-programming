# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        current=head
        
        while current:
            temp2=current
            temp=current.next
            current.next=pre
            pre=temp2
            current=temp
            
          
        
        return pre
                