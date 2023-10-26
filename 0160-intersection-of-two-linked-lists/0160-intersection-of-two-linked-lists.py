# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        res = None
        visited = set()
        
        while headA or headB:
            if headA == headB:
                res = headA
                break
                
            elif headA in visited:
                res = headA
                break
                
            elif headB in visited:
                res = headB
                break
            
            if headA:
                visited.add(headA)
                headA = headA.next
                
            
            if headB:
                visited.add(headB)    
                headB = headB.next
            
        return res