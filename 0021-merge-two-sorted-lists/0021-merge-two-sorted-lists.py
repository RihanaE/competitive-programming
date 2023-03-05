# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy
        res = self.helper(list1, list2,res)
        
        return dummy.next
        
    def helper(self, h1, h2, res):
        if h1 == None and h2 != None:
            res.next = h2
            return res
        
        elif h2 == None and h1 != None:
            res.next = h1
            return res
        
        elif h2 == None and h1 == None:
            return res
        
        else:
            if h1.val < h2.val:
                res.next = ListNode(h1.val)
                h1 = h1.next
                
            else:
                res.next = ListNode(h2.val)
                h2 = h2.next
                
            res = res.next
            
            return self.helper(h1, h2, res)