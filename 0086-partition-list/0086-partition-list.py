# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = []
        greater = []
        curr = head
        dummy = ListNode(0)
        
        while curr:
            if curr.val >= x:
                greater.append(curr.val)
                
            else:
                less.append(curr.val)
                
            curr = curr.next
            
        temp = dummy
        for i in less:
            temp.next = ListNode(i)
            temp = temp.next
            
        for i in greater:
            temp.next = ListNode(i)
            temp = temp.next
            
            
        return dummy.next