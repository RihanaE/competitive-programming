# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = True
        
        while flag:
            pre = head
            if head:
                curr = head.next
            else:
                curr = None
                
            swap = False
            
            while curr:
                if pre.val > curr.val:
                    curr.val, pre.val = pre.val, curr.val
                    swap = True
                    
                pre = pre.next
                curr = curr.next
                
            if swap == False:
                flag = False
                
            
        return head