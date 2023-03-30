# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        left = 0 
        right = len(arr) - 1
        mx = 0
        
        while left < right:
            if arr[left] + arr[right] > mx:
                mx = arr[left] + arr[right]
                
            left += 1
            right -= 1
            
        return mx