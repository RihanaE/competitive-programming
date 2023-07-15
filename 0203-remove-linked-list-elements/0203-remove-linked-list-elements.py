# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        
        def helper(head):
            nonlocal temp 
            
            if not head:
                return 
            
            elif head.val == val:
                head = head.next
                return helper(head)
            
            temp.next = ListNode(head.val)
            temp = temp.next
            return helper(head.next)
        
        helper(head)
        return dummy.next