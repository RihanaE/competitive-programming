# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0, head)
        pre,cur=dummy, head

        while cur and cur.next:
            temp1=cur.next.next
            temp2=cur.next

            temp2.next=cur
            cur.next=temp1
            pre.next=temp2

            pre=cur
            cur=temp1

        return dummy.next