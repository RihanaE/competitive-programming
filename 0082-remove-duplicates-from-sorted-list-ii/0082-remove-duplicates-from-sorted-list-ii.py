# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode()
        curr = head
        res = pre
        
        while curr:
            if curr.next and curr.val != curr.next.val:
               
                pre.next = ListNode(curr.val)
                pre = pre.next
                    
                curr = curr.next
                
            elif curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                    
                curr = curr.next
               
                
            else:
                pre.next = ListNode(curr.val)
                pre = pre.next
                curr = curr.next
                
        return res.next