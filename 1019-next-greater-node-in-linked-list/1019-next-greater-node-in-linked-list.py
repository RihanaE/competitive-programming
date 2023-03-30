# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        size = 0
        
        while curr:
            size += 1
            curr = curr.next
            
        res = [0] * size
        stack = []
        pointer = 0
        
        while head:
            if not stack:
                stack.append([head.val, pointer])
                
            elif stack[-1][0] >= head.val:
                stack.append([head.val, pointer])
                
            
            else:
                while stack and stack[-1][0] < head.val:
                    res[stack[-1][1]] = head.val
                    stack.pop()
                    
                stack.append([head.val, pointer])
                
            pointer += 1
            head = head.next
            
        return res