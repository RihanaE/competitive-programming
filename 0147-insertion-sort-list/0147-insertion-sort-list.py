# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0 , head)
        pre, current=head,head.next
        
        while current:
            if current.val >= pre.val:
                pre, current=current, current.next
                continue
                
                
            temp=dummy
            
            while current.val > temp.next.val:
                temp=temp.next
                
            pre.next=current.next
            current.next=temp.next
            temp.next=current
            current=pre.next
            
            
        return dummy.next