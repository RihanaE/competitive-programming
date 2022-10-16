# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
    
        def size(head):
            current=head
            size=0
            
            while current:
                size +=1
                current=current.next
                
            return size
        
        s=size(head)
        current = head
        i= 0
        while i < s - n:
            
            if i == s - n - 1:
                temp=current.next.next
                current.next=temp
                
                
            current=current.next
            i +=1
        if s <= n:
            head=head.next
        
        return head