# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
            
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
            
        res = int("".join(num1)) + int("".join(num2))
        ans = ListNode(0)
        dummy = ans
        
        for i in str(res):
            dummy.next = ListNode(int(i))
            
            dummy = dummy.next
            
        return ans.next