# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        template = dummy
        remain = 0
        
        while cur1 and cur2:
            temp = cur1.val + cur2.val
            if temp + remain >= 10:
                print(dummy.next, remain)
                value = (temp + remain) % 10
                remain = 1
                
            else:
                value = temp % 10 + remain
                remain = 0
                
            template.next = ListNode(value)
            template = template.next
            cur1 = cur1.next
            cur2 = cur2.next
            
#             if temp % 10 != 0:
#                 remain = 1
                
#             else:
#                 remain = 0
                
        while cur1:
            temp = cur1.val
            if temp + remain >= 10:
                value = (temp + remain) % 10
                remain = 1
                
            else:
                value = temp % 10 + remain
                remain = 0
                
            template.next = ListNode(value)
            template = template.next
            cur1 = cur1.next
            
        while cur2:
            temp = cur2.val
            if temp + remain >= 10:
                value = (temp % 10 + remain) % 10
                remain = 1
                
            else:
                value = temp % 10 + remain
                remain = 0
                
            template.next = ListNode(value)
            template = template.next
            cur2 = cur2.next
            
        if remain != 0:
            template.next = ListNode(remain)
            
        return dummy.next
            