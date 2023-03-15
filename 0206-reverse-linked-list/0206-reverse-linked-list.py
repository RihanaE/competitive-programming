# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)
    
    def helper(self, curr,ans = None, prev = None):
        if not curr:
            return ans
        
        temp = curr.next
        curr.next = prev
        prev = curr
        ans = curr
        
        return self.helper(temp, ans, prev)