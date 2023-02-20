# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        curr = head
        
        while curr:
            curr = curr.next
            size += 1
            
        for i in range(size // 2):
            head = head.next
            
        return head