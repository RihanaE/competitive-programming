# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        current=head
        
        while current:
            stack.append(current.val)
            current=current.next
            
        i=0
        j=len(stack) -1
        res=0
        
        while i < j:
            res=max(res, stack[i] + stack[j])
            j -=1
            i +=1
        return res