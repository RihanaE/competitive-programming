# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = [0]
        prefixSum = [0]
        
        while head:
            if prefixSum[-1] + head.val in prefixSum:
                temp = prefixSum[-1] + head.val
                while prefixSum and prefixSum[-1] != temp:
                    prefixSum.pop()
                    ans.pop()
                    
            else:
                prefixSum.append(prefixSum[-1] + head.val)
                ans.append(head.val)
                
            head = head.next
            
        dummy = ListNode(0)
        curr = dummy
        
        for i in ans[1:]:
            curr.next = ListNode(i)
            curr = curr.next
            
        return dummy.next