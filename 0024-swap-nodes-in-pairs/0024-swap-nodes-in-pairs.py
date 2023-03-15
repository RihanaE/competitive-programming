# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)
        # return head÷
        
    def helper(self, tracker):
        curr = tracker
        if tracker == None:
            return
        
        elif tracker and not tracker.next:
            return tracker
        
        else:
            pre = curr
            temp = curr.next.next
            curr = curr.next
            curr.next = pre
            
            curr.next.next = self.helper(temp)
            
            # curr.next.next = curr
            # curr.next = temp
            
            
            
            return curr
            