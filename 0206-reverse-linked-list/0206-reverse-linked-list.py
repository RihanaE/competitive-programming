# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        out = ListNode()
        res = out
        for i in range(len(arr) - 1, -1, -1):
            res.next = ListNode(arr[i])
            res = res.next
            
        return out.next