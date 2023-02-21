# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        
        while curr:
            size +=1
            curr = curr.next
            
        if size == 1:
            return None
        
        length = size - n
        dummy = ListNode(0, head)
        curr = dummy
        
        for i in range(length):
            curr = curr.next
            
        curr.next = curr.next.next
        
        return dummy.next