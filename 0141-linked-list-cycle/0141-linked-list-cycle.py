# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        store = set()
        curr = head
        
        while curr:
            if curr in store:
                return True
            
            store.add(curr)
            curr = curr.next
            
        return False