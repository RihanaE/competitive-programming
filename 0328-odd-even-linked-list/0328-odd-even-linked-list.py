# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode()
        curr = dummy
        
        odd = head
        even = None
        
        if head.next:
            even = head.next
            
        while odd:
            curr.next = ListNode(odd.val)
            curr = curr.next
            
            odd = odd.next
            if odd:
                odd = odd.next
                
        while even:
            curr.next = ListNode(even.val)
            curr = curr.next
            
            even = even.next
            if even:
                even = even.next
                
        return dummy.next