# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head == None:
        #     return head
        res = head
        
        
        while res and res.next:
            if res.next and res.val != res.next.val:
                res = res.next
                
            else:
                while res.next and res.val == res.next.val:
                    res.next = res.next.next
                    
        return head