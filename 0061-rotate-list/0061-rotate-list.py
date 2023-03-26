# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        size = 0
        if not head:
            return head
        
        while curr:
            size += 1
            curr = curr.next
            
        if k % size == 0:
            return head
        
        k = k % size
        limit = size - k
        curr = head
        
        for i in range(limit - 1):
            curr = curr.next
            
        pre = curr.next
        res = pre
        curr.next = None
        
        while pre.next:
            pre = pre.next
            
        pre.next = head
        return res